print("cli.py loaded")

import argparse

from splitter.scanner import scan_directory


def main():
    parser = argparse.ArgumentParser(
        prog="chapter-media-splitter",
        description="Split chaptered MKV TV releases into individual episodes."
    )

    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a directory for MKV files."
    )

    scan_parser.add_argument(
        "directory",
        help="Directory to scan."
    )

    args = parser.parse_args()

    if args.command == "scan":
        scan_directory(args.directory)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()