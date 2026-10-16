#!/usr/bin/env python3
"""Adapt the pinned helium-linux checkout for unsigned GitHub-hosted fork builds.

Run from the platform repository root, with this fork in helium-chromium/.
Keep replacements strict so a tooling update cannot silently change behavior.
"""

from pathlib import Path


def replace_once(filename, before, after):
    path = Path(filename)
    content = path.read_text(encoding="utf-8")
    if content.count(before) != 1:
        raise SystemExit(f"Unexpected platform tooling in {filename}: {before!r}")
    path.write_text(content.replace(before, after, 1), encoding="utf-8")


# Avoid downloading PGO profiles and expensive release optimizations on small VMs.
replace_once(".github/scripts/build.sh", "fetch_sources false true",
             "fetch_sources false false")
replace_once("flags.linux.gn", "is_official_build=true", "is_official_build=false")
replace_once("flags.linux.gn", "symbol_level=1", "symbol_level=0")
with Path("flags.linux.gn").open("a", encoding="utf-8") as flags:
    flags.write("\nuse_thin_lto=false\n")

# A fork AppImage must not advertise updates from imputnet/helium-linux.
replace_once("scripts/package.sh", '    -u "$_update_info" \\\n', "")

# Leave space for extracting source/build artifacts after loading the image.
replace_once(".github/actions/build/action.yml",
             "run: docker load -i /tmp/chromium-builder.tar",
             "run: |\n        docker load -i /tmp/chromium-builder.tar\n"
             "        rm /tmp/chromium-builder.tar")

# Intermediate artifacts must survive a multi-day compilation run.
replace_once(".github/actions/build/action.yml", "        overwrite: true",
             "        overwrite: true\n        retention-days: 7\n"
             "        compression-level: 0")

# New Chromium versions may not have a Linux tarball yet. Match the existing
# source-validation CI by falling back to the fork's Chromium clone utility.
replace_once(
    "scripts/shared.sh",
    '''        "${_main_repo}/utils/downloads.py" retrieve -i "${_main_repo}/downloads.ini" "${_root_dir}/downloads.ini" -c "${_dl_cache}"
        "${_main_repo}/utils/downloads.py" unpack -i "${_main_repo}/downloads.ini" "${_root_dir}/downloads.ini" -c "${_dl_cache}" "${_src_dir}"''',
    '''        if "${_main_repo}/utils/downloads.py" retrieve -i "${_main_repo}/downloads.ini" "${_root_dir}/downloads.ini" -c "${_dl_cache}"; then
            "${_main_repo}/utils/downloads.py" unpack -i "${_main_repo}/downloads.ini" "${_root_dir}/downloads.ini" -c "${_dl_cache}" "${_src_dir}"
        else
            "${_main_repo}/utils/clone.py" --sysroot amd64 -o "${_src_dir}"
            # clone.py deliberately skips most binary build dependencies.
            python3 "${_main_repo}/utils/install_cipd_deps.py" "${_src_dir}"
            python3 "${_src_dir}/tools/clang/scripts/update.py"
            python3 "${_src_dir}/tools/rust/update_rust.py"
            python3 "${_src_dir}/third_party/node/update_node_binaries.py"
            python3 "${_src_dir}/build/linux/sysroot_scripts/install-sysroot.py" --arch=amd64
            # Keep depot_tools/CIPD tools, but discard Git histories before caching.
            find "${_src_dir}" -type d -name .git -prune -exec rm -rf {} +
            rm -rf "${_src_dir}/uc_staging"
        fi''',
)
