from pathlib import Path
import subprocess


def build_split_command(
    input_file: Path,
    output_file: Path,
) -> list[str]:
    """
    Build the mkvmerge command used to split an MKV by chapters.
    """
    return [
        "mkvmerge",
        "-o",
        str(output_file),
        "--split",
        "chapters:all",
        str(input_file),
    ]


def split_mkv(
    input_file: Path,
    output_dir: Path,
) -> list[Path]:
    """
    Split an MKV into separate files using chapter boundaries.

    Returns a sorted list of the generated MKV files.
    """

    # Ensure the output directory exists.
    output_dir.mkdir(parents=True, exist_ok=True)

    # mkvmerge will create:
    # episode-001.mkv
    # episode-002.mkv
    # etc.
    output_file = output_dir / "episode.mkv"

    command = build_split_command(input_file, output_file)

    subprocess.run(
        command,
        check=True,
    )

    return sorted(output_dir.glob("*.mkv"))