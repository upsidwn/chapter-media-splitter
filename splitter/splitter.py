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

    Returns a sorted list of generated MKV files.
    """

    # Verify the input file exists.
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # Create the output directory if it doesn't exist.
    output_dir.mkdir(parents=True, exist_ok=True)

    # mkvmerge will create:
    # episode-001.mkv
    # episode-002.mkv
    output_file = output_dir / "episode.mkv"

    command = build_split_command(input_file, output_file)

    try:
        subprocess.run(
            command,
            check=True,
        )

    except FileNotFoundError:
        raise RuntimeError(
            "mkvmerge was not found. Please install MKVToolNix."
        )

    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"mkvmerge failed with exit code {exc.returncode}"
        ) from exc

    files = sorted(output_dir.glob("*.mkv"))

    if not files:
        raise RuntimeError("No output files were generated.")

    return files