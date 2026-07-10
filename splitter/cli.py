import argparse
from pathlib import Path

from splitter.scanner import scan_directory
from splitter.metadata import inspect_file, summarize_metadata
from splitter.detection import detect_chaptered_release
from splitter.splitter import split_mkv


def main():
    parser = argparse.ArgumentParser(
        prog="chapter-media-splitter",
        description="Split chaptered MKV TV releases into individual episodes."
    )

    subparsers = parser.add_subparsers(dest="command")

    # Scan command
    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a directory for MKV files."
    )

    scan_parser.add_argument(
        "directory",
        help="Directory to scan."
    )

    # Inspect command
    inspect_parser = subparsers.add_parser(
        "inspect",
        help="Inspect an MKV file."
    )

    inspect_parser.add_argument(
        "file",
        help="MKV file to inspect."
    )

    # Split command
    split_parser = subparsers.add_parser(
        "split",
        help="Split a chaptered MKV into individual files."
    )

    split_parser.add_argument(
        "file",
        help="MKV file to split."
    )

    split_parser.add_argument(
        "output",
        help="Directory for the split files."
    )

    args = parser.parse_args()

    if args.command == "scan":
        try:
            mkv_files = scan_directory(args.directory)
            if mkv_files:
                print(f"\nFound {len(mkv_files)} MKV file(s):\n")
                for file in mkv_files:
                    size_mb = file.stat().st_size / (1024 * 1024)
                    print(f"• {file.name}")
                    print(f"  Path : {file.parent}")
                    print(f"  Size : {size_mb:.1f} MB\n")
            else:
                print("No MKV files found.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    elif args.command == "inspect":
        metadata = inspect_file(args.file)
        detection = detect_chaptered_release(metadata)

        print(summarize_metadata(metadata))

        print("\nAnalysis")
        print("--------")
        print(f"Likely Chaptered Release : {detection.is_chaptered}")
        print(f"Estimated Episodes       : {detection.estimated_episodes}")
        print(f"Confidence               : {detection.confidence}")
        print(f"Reason                   : {detection.reason}")

    elif args.command == "split":
        try:
            files = split_mkv(
                Path(args.file),
                Path(args.output),
            )

            print(f"\nCreated {len(files)} file(s):\n")

            for file in files:
                print(f"• {file.name}")

        except (FileNotFoundError, RuntimeError) as e:
            print(f"Error: {e}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()