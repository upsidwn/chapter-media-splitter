# Chapter Media Splitter

## Goal

Split chapter-based MKV TV season releases into Sonarr-compatible episode files.

---

## Current Features

- Episode splitting
- Recursive MKV scanning
- Metadata inspection
- Runtime formatting
- Chapter detection
- Episode estimation
- Split chaptered MKV files into individual episode files using MKVToolNix.
- Episode Renaming complete

---

## Planned/Next Features

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
    Splits MKVs using MKVToolNix

renamer.py
    Will rename episodes

---

## Coding Standards

- Use pathlib instead of os.path
- Return data instead of printing from library modules
- Keep functions small
- One responsibility per module