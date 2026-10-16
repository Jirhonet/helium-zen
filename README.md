<div align="center">
    <img src="resources/branding/app_icon/raw.png"
        title="Helium (Zen)" alt="Helium (Zen) logo" width="120" />
    <h1>Helium (Zen)</h1>
    <p>
        The Chromium-based web browser made for people, with love.
        <br>
        Privacy-first with unbiased ad-blocking. No bloat and no noise.
    </p>    
	<p>
		Helium (Zen) is an AI-slop fork of Helium, adding workspaces and a full sidebar experience like in Zen.
	</p>
	<a href="https://helium.computer/">
        helium.computer
    </a>
</div>

## Downloads
> [!NOTE]
> Helium is in beta, so unexpected issues may occur.
> Please report them if they haven't already been reported.

The easiest way to download Helium is [helium.computer](https://helium.computer/).
It'll pick a compatible binary for your platform automatically.

The same releases can also be downloaded from source on GitHub:

- [Latest macOS release](https://github.com/imputnet/helium-macos/releases/latest)
- [Latest Linux release](https://github.com/imputnet/helium-linux/releases/latest)
- [Latest Windows release](https://github.com/imputnet/helium-windows/releases/latest)

Helium supports automatic updates on macOS and Windows.

## Helium repos
All Helium packaging, tooling, services, and components are open source
and published on GitHub.

### Platform packaging and tooling
- [Helium for macOS](https://github.com/imputnet/helium-macos)
- [Helium for Linux](https://github.com/imputnet/helium-linux)
- [Helium for Windows](https://github.com/imputnet/helium-windows)

### Web services
[Helium services](https://github.com/imputnet/helium-services) are Helium's
privacy-first cloud services that handle the extension proxy, !bangs, filter
lists, browser updates, crash reports, and etc. The services are self-hostable
and the repo includes exactly what we use and host, down to Ansible playbooks.

### Components
- [Helium uBlock Origin](https://github.com/imputnet/uBlock) is a
Helium-specific fork of uBlock Origin that includes our filters, defaults, and
CNAME uncloaking.

- [Helium onboarding](https://github.com/imputnet/helium-onboarding) includes
the browser setup experience seen at `helium://setup` on first launch.

- [Helium non-free assets](https://github.com/imputnet/helium-nonfree-assets)
repo handles non-free assets used in Helium, such as search engine icons and
icons of other browsers.

### Tooling
- [Chromium tarballs](https://github.com/imputnet/chromium-tarballs) creates
prepared Chromium source archives used by Helium builds.

- [Helium Prism](https://github.com/imputnet/helium-prism) is a Svelte UI
Component library used in onboarding and the landing page.

### Legal documents
[Helium Legal](https://github.com/imputnet/helium-legal) repo includes the
source for [Terms of Use](https://helium.computer/terms) and
[Privacy Policy](https://helium.computer/privacy) documents, along with their
full change history.

## Development
macOS and Linux are our primary development platforms, so they're the
recommended development environment for community contributions.

[> See development docs in macOS repo](https://github.com/imputnet/helium-macos/blob/main/docs/building.md#development-build-and-environment)

Linux packaging includes a similar development script, so the same guide
can be applied there too.

[> See development docs in macOS repo](https://github.com/imputnet/helium-macos/blob/main/docs/building.md#development-build-and-environment)

## Build your own Linux version

The **Build Linux x86_64** GitHub Actions workflow builds this fork on
GitHub-hosted Ubuntu runners. Commit and push the workflow to your fork's default
branch, then open **Actions → Build Linux x86_64 → Run workflow**. Select the
branch to build and start the run.

When the `package` job succeeds, download `helium-zen-linux-x86_64-<commit>` from
the run's **Artifacts** section. It contains an unsigned AppImage, a `.tar.xz`
archive, and a `.deb` package. Extract the downloaded artifact ZIP first; for the
AppImage, run `chmod +x helium-*.AppImage` before launching it. No signing secrets
or local build machine are required.

The workflow checks out this fork at the selected commit inside the Linux build
tooling, pinned to `imputnet/helium-linux` commit
`b154afccb44729359c816754c7741efb3cb8f497`. It falls back to cloning Chromium if
source archives are unavailable. Builds use reduced optimization and omit debug
symbols and PGO to reduce resource requirements. The AppImage does not advertise
updates from upstream Helium.

Chromium compilation can take many hours. Up to ten five-hour compilation jobs
resume the same build through intermediate artifacts, leaving time within
GitHub's six-hour job limit to restore and save progress. Unneeded compilation
jobs are skipped after completion. Intermediate artifacts expire after seven
days; downloadable packages expire after fourteen days. Source/build artifacts
are large, so check your account's artifact storage and Actions usage allowance,
especially for private repositories. Runner disk or memory limits can still
cause a build to fail.

When updating the pinned Linux tooling, review
`.github/scripts/configure-linux-build.py` as well: its strict replacements fail
if the expected platform scripts change.
## Contributing
Before contributing to Helium, please read the guidelines in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

### The Chromium project
[The Chromium Project](https://www.chromium.org/) is at the core of Helium,
making it possible in the first place.

### ungoogled-chromium
Helium originally branched off
[ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium).
Special thanks to everyone behind ungoogled-chromium, they made working with
Chromium much easier.

### Other Chromium projects

Helium includes some patches from other open source Chromium projects:

- [Inox patchset](https://github.com/gcarq/inox-patchset)
- [Debian](https://tracker.debian.org/pkg/chromium-browser)
- [Bromite](https://github.com/bromite/bromite)
- [Iridium Browser](https://iridiumbrowser.de/)
- [Brave](https://github.com/brave/brave-core)

All patches are sorted by vendor in the [patches](patches/) directory of this repo.

## License
All code, patches, modified portions of imported code or patches, and
any other content that is unique to Helium and not imported from other
repositories is licensed under GPL-3.0. See [LICENSE](LICENSE).

Any content imported from other projects retains its original license (for
example, any original unmodified code imported from ungoogled-chromium remains
licensed under their [BSD 3-Clause license](LICENSE.ungoogled_chromium)).
