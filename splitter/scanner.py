from pathlib import Path


def scan_directory(directory):
    directory = Path(directory)

    if not directory.exists():
        print(f"❌ Directory does not exist: {directory}")
        return

    mkv_files = sorted(directory.rglob("*.mkv"))

    if not mkv_files:
        print("No MKV files found.")
        return

    print(f"\nFound {len(mkv_files)} MKV file(s):\n")

    for file in mkv_files:
        size_mb = file.stat().st_size / (1024 * 1024)

        print(f"• {file.name}")
        print(f"  Path : {file.parent}")
        print(f"  Size : {size_mb:.1f} MB\n")