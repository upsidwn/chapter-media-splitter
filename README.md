# Chapter Media Splitter

Python CLI utility for converting chaptered MKV TV season releases into individually named episodes compatible with Sonarr, Jellyfin, Plex, and other media managers.

---

## Why I Built This

Some TV releases package an entire season into a single MKV with chapter markers instead of separate episode files. This project automates converting those releases into individual episodes using MKVToolNix and prepares them for import into media managers like Sonarr and Jellyfin.

The project was inspired by solving a real world problem in my home lab and serves as a portfolio project demonstrating Python, automation, and CLI application development.

## Features

- Detect chaptered MKV files
- Split episodes using MKVToolNix
- Generate Sonarr-compatible filenames
- Support configurable output locations
- Cross-platform (Linux, macOS, Windows)

## Roadmap

- [x] Scan directories for MKV files
- [x] Read chapter metadata
- [ ] Split MKVs automatically
- [ ] Rename episodes
- [ ] Configuration file support
- [ ] Dry-run mode
- [ ] Logging
- [ ] Unit tests
- [ ] GitHub Actions CI

## Technologies

- Python 3
- MKVToolNix (`mkvmerge`)
- argparse
- pathlib
- subprocess
- logging
- pytest

## Installation

*(add this later.)*

## Usage

*(add this later.)*

## Example

*(add this later.)*

## License

MIT