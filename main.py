"""
main.py

CLI entry point for the Smart File Organizer.
Handles user input, directory validation, and optional dry-run mode.
"""

from pathlib import Path
from organizer import organize


def main() -> None:
    """
    Main function to run the Smart File Organizer.

    Behavior:
        - Prompts the user for a directory path.
        - Validates that the path exists and is a directory.
        - Prompts the user whether to run in dry-run mode.
        - Calls the organize function with the chosen settings.
        - Prints the final status message.
    """
    # Prompt user for the directory to organize
    path_input = input("Enter directory to organize: ").strip()
    directory = Path(path_input)

    # Validate that the path exists and is a directory
    if not directory.exists() or not directory.is_dir():
        print("❌ Invalid directory path.")
        return

    # Prompt user for dry-run mode
    dry_input = input("Dry-run mode? (y/n): ").strip().lower()
    dry_run = dry_input == 'y'  # True if user entered 'y', else False

    # Run the organizer with or without dry-run
    organize(directory, dry_run=dry_run)

    # Print final status message
    if dry_run:
        print("✅ Dry-run complete. No files were moved.")
    else:
        print("✅ Files organized successfully.")


if __name__ == "__main__":
    main()
