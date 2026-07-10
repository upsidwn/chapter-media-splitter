from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RenameOperation:
    """
    Represents a planned file rename.
    """

    source: Path
    destination: Path


def build_episode_filenames(
    files: list[Path],
    show_name: str,
    season: int,
) -> list[RenameOperation]:
    """
    Build a list of planned episode filenames.

    This function does not rename any files.
    It only determines what the filenames should be.
    """

    operations: list[RenameOperation] = []

    for episode_number, source in enumerate(sorted(files), start=1):
        new_filename = (
            f"{show_name}."
            f"S{season:02d}"
            f"E{episode_number:02d}"
            f"{source.suffix}"
        )

        destination = source.with_name(new_filename)

        operations.append(
            RenameOperation(
                source=source,
                destination=destination,
            )
        )

    return operations