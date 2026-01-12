"""
organizer.py

Core logic for organizing files inside a directory.
Responsible for categorization, duplicate handling,
recursive traversal, and safe file movement.

Features:
- Recursively scans all subfolders
- Organizes files into categories (Documents, Images, etc.)
- Prevents overwriting by resolving duplicate names
- Supports dry-run mode to simulate actions
- Logs all operations
"""

from pathlib import Path
from config import FILE_CATEGORIES
from utils import ensure_folder
from logger import get_logger

# Initialize logger
logger = get_logger()


def get_category(file_path: Path) -> str:
    """
    Determine the category for a given file based on its extension.

    Args:
        file_path (Path): The file to categorize.

    Returns:
        str: The category name.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if file_path.suffix.lower() in extensions:
            return category
    # Default category if no match is found
    return "Others"


def resolve_duplicate(target_path: Path, planned_paths: set) -> Path:
    """
    Resolve duplicate file names by appending a counter.

    Example:
        file.txt -> file_1.txt -> file_2.txt

    Args:
        target_path (Path): Intended destination path.
        planned_paths (set): Set of destination paths already planned
                             in this run (for dry-run simulation).

    Returns:
        Path: A non-existing destination path.
    """
    counter = 1
    new_path = target_path

    # Keep incrementing until the path is unique (either on disk or planned)
    while new_path.exists() or new_path in planned_paths:
        new_name = f"{target_path.stem}_{counter}{target_path.suffix}"
        new_path = target_path.parent / new_name
        counter += 1

    return new_path


def organize(directory: Path, dry_run: bool = False) -> None:
    """
    Organize files in the given directory into categorized folders.

    Args:
        directory (Path): Directory whose files will be organized.
        dry_run (bool): If True, simulate organization without moving files.

    Behavior:
        - Recursively scans all subfolders.
        - Skips category folders to avoid infinite loops.
        - Prevents overwriting files by handling duplicates.
        - Moves files unless dry_run=True.
        - Logs all operations.
        - Dry-run mode shows final duplicate names correctly.
    """
    category_names = set(FILE_CATEGORIES.keys()) | {"Others"}
    planned_paths = set()  # Tracks destination paths to handle duplicates in dry-run

    # Recursively iterate over all items
    for item in directory.rglob("*"):

        # Skip directories
        if not item.is_file():
            continue

        # Skip files already inside category folders
        if item.parent.name in category_names:
            continue

        # Determine category for this file
        category = get_category(item)

        # Ensure target folder exists
        target_dir = directory / category
        ensure_folder(target_dir)

        # Determine initial target path
        target_path = target_dir / item.name

        # Resolve duplicates (accounts for both existing files and planned moves)
        final_path = resolve_duplicate(target_path, planned_paths)

        # Add this final_path to planned_paths to prevent conflicts in this run
        planned_paths.add(final_path)

        if dry_run:
            # Dry-run mode: log and print the planned action
            print(
                f"[DRY-RUN] Would move '{item.relative_to(directory)}' "
                f"to '{category}/{final_path.name}'"
            )
            logger.info(
                f"[DRY-RUN] '{item}' -> '{category}/{final_path.name}'"
            )
        else:
            # Perform the actual file move
            item.rename(final_path)
            logger.info(
                f"Moved '{item}' to '{category}/{final_path.name}'"
            )
