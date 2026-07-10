from pathlib import Path
import subprocess


def build_split_command(
    input_file: Path,
    output_file: Path,
) -> list[str]:
    return [
        "mkvmerge",
        "-o",
        str(output_file),
        "--split",
        "chapters:all",
        str(input_file),
    ]
def run_split_command(command: list[str]) -> subprocess.CompletedProcess:
    ...


def split_mkv(input_file: Path, output_dir: Path):
    ...