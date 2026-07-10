# Chapter Media Splitter

Python CLI utility for converting chaptered MKV TV season releases into individually named episodes compatible with Sonarr, Jellyfin, Plex, and other media managers.

---

## Why I Built This

Some TV releases package an entire season into a single MKV with chapter markers instead of separate episode files. This project automates converting those releases into individual episodes using MKVToolNix and prepares them for import into media managers like Sonarr and Jellyfin.

The project was inspired by solving a real world problem in my home lab and serves as a portfolio project demonstrating Python, automation, and CLI application development.

## Features
## Current Features

- Scan directories recursively for MKV files
- Inspect MKV metadata
- Display formatted media information
- Detect likely chaptered TV season releases
- Estimate episode count
- Split chaptered MKV files into individual episode files

## Roadmap

- [x] Scan directories for MKV files
- [x] Read MKV metadata
- [x] Detect chaptered TV season releases
- [x] Split MKVs into individual episodes
- [ ] Rename episodes for Sonarr
- [ ] Dry-run mode
- [ ] Configuration file
- [ ] Logging
- [ ] Unit tests
- [ ] GitHub Actions

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

Scan a directory:

```bash
python -m splitter.cli scan /path/to/media
```

Inspect an MKV:

```bash
python -m splitter.cli inspect /path/to/file.mkv
```

Split an MKV:

```bash
python -m splitter.cli split /path/to/file.mkv output/
```

## Example

*(add this later.)*

## License

MIT