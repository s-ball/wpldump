# wpldump

## Description

This aims at extracting automatically the metadata from the .wav files contained in a playlist.

## Installation

[TO BE DONE]

#### Special handling of `version.py`:

`wpldump` relies on `setuptools-scm` to automatically extract a
version number from git metadata and store it in a `version.py` file
for later use. This requires the availability of both `git` (which should
not be a problem when the project is downloaded from GitHub), and
`setuptools-scm`. If it fails because one is not available or because
git metadata is not there (if you only downloaded a zip archive from
GitHub), the version is set to 0.0.0

For that reason, if you do not use git to download the sources, you
should download a source distribution from PyPI, because the latter
contains a valid `version.py`

`pip` uses the `pyproject.toml` file with respect to PEP-518 and
PEP-517 to know that `setuptools-scm` is required before the build.

## Contributions

Contributions are welcome, including issues on GitHub.
Problems are expected to be documented so that they can be reproduced. But
I only develop this on my free time, so I cannot guarantee quick answers...

## Disclaimer: alpha quality

This is currently a *work in progress*

## License

This work is licenced under a MIT Licence. See [LICENSE.txt](https://raw.githubusercontent.com/s-ball/wpldump/master/LICENCE.txt)
