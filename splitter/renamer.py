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


def rename_files(
    operations: list[RenameOperation],
) -> list[Path]:
    """
    Execute a list of planned file rename operations.

    Returns a list of the renamed file paths.
    """

    renamed_files: list[Path] = []

    for operation in operations:
        if operation.destination.exists():
            raise FileExistsError(
                f"Destination file already exists: {operation.destination}"
            )

        operation.source.rename(operation.destination)
        renamed_files.append(operation.destination)

    return renamed_files