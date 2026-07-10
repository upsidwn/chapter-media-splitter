import argparse
from pathlib import Path

from splitter.scanner import scan_directory
from splitter.metadata import inspect_file, summarize_metadata
from splitter.detection import detect_chaptered_release
from splitter.splitter import split_mkv
from splitter.renamer import (
    build_episode_filenames,
    rename_files,
)


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

    # Rename command
    rename_parser = subparsers.add_parser(
        "rename",
        help="Rename split MKV files."
    )

    rename_parser.add_argument(
        "directory",
        help="Directory containing split MKV files."
    )

    rename_parser.add_argument(
        "--show-name",
        required=True,
        help="Show name."
    )

    rename_parser.add_argument(
        "--season",
        required=True,
        type=int,
        help="Season number."
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

    elif args.command == "rename":
        try:
            directory = Path(args.directory)

            files = sorted(directory.glob("*.mkv"))

            if not files:
                raise FileNotFoundError(
                    "No MKV files found in the specified directory."
                )

            operations = build_episode_filenames(
                files,
                args.show_name,
                args.season,
            )

            renamed_files = rename_files(operations)

            print(f"\nRenamed {len(renamed_files)} file(s):\n")

            for file in renamed_files:
                print(f"• {file.name}")

        except (
            FileNotFoundError,
            FileExistsError,
        ) as e:
            print(f"Error: {e}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()