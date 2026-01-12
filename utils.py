"""
utils.py

Utility/helper functions used across the project.
These functions focus on safety and reusability.
"""

from pathlib import Path


def ensure_folder(folder: Path) -> None:
    """
    Ensure that a folder exists.

    If the folder does not exist, it will be created.
    If it already exists, nothing happens.

    Args:
        folder (Path): The directory path to ensure.
    """
    folder.mkdir(exist_ok=True)
