import argparse
import json

from splitter.scanner import scan_directory
from splitter.metadata import inspect_file
from splitter.metadata import inspect_file, summarize_metadata

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

    args = parser.parse_args()

    if args.command == "scan":
        scan_directory(args.directory)

    elif args.command == "inspect":
        metadata = inspect_file(args.file)
        print(summarize_metadata(metadata))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()