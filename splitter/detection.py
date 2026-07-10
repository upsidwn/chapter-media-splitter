from dataclasses import dataclass


@dataclass
class DetectionResult:
    """Represents the results of chaptered release detection."""

    is_chaptered: bool
    estimated_episodes: int
    confidence: str
    reason: str


def detect_chaptered_release(metadata):
    """
    Determine whether an MKV appears to be a chaptered TV season.

    Version 1 uses a simple heuristic:
    - Runtime >= 45 minutes
    - At least 10 chapters
    """

    duration_ns = metadata["container"]["properties"]["duration"]
    chapters = metadata["chapters"][0]["num_entries"]

    duration_minutes = duration_ns / 1_000_000_000 / 60

    if duration_minutes >= 45 and chapters >= 10:
        return DetectionResult(
            is_chaptered=True,
            estimated_episodes=max(chapters - 1, 1),
            confidence="Medium",
            reason="Long runtime with many chapters."
        )

    return DetectionResult(
        is_chaptered=False,
        estimated_episodes=0,
        confidence="Low",
        reason="Does not resemble a chaptered TV season."
    )