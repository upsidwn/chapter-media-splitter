# Chapter Media Splitter

## Goal

Split chapter-based MKV TV season releases into Sonarr-compatible episode files.

---

## Current Features

- Directory scanning
- MKV metadata inspection

---

## Planned Features

- Chapter detection
- Episode splitting
- Episode renaming
- Config file
- Logging
- Dry-run mode
- Unit tests
- GitHub Actions

---

## Architecture

cli.py
    Handles CLI arguments

scanner.py
    Finds MKV files

metadata.py
    Reads metadata via mkvmerge

splitter.py
    Will split MKVs

renamer.py
    Will rename episodes

---

## Coding Standards

- Use pathlib instead of os.path
- Return data instead of printing from library modules
- Keep functions small
- One responsibility per module