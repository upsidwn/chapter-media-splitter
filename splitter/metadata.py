import json
import subprocess
from pathlib import Path


def inspect_file(file_path):
    """Return MKV metadata as a Python dictionary."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    result = subprocess.run(
        [
            "mkvmerge",
            "-J",
            str(file_path)
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return json.loads(result.stdout)

def summarize_metadata(metadata):
    """Return a human-readable summary of MKV metadata."""

    lines = []

    lines.append(f"File: {Path(metadata['file_name']).name}")
    lines.append(f"Container: {metadata['container']['type']}")

    duration_ns = metadata["container"]["properties"]["duration"]
    lines.append(
    f"Duration: {format_duration(duration_ns)}"
)

    chapters = metadata["chapters"][0]["num_entries"]
    lines.append(f"Chapters: {chapters}")

    lines.append("")
    lines.append("Tracks:")

    for track in metadata["tracks"]:
        lines.append(f"  {track['type']}: {track['codec']}")

    return "\n".join(lines)

def format_duration(duration_ns):
    """Convert nanoseconds to HH:MM:SS."""

    total_seconds = duration_ns // 1_000_000_000

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"