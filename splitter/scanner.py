from pathlib import Path


def scan_directory(directory):
    """Scan directory for MKV files and return sorted list."""
    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    mkv_files = sorted(directory.rglob("*.mkv"))
    return mkv_files