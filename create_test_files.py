"""
create_test_files.py

Utility script to quickly generate sample files for testing
the Smart File Organizer.
"""

from pathlib import Path

TEST_DIR = Path("test_folder")

FILES = [
    "photo1.jpg",
    "photo2.png",
    "document1.pdf",
    "document2.docx",
    "song1.mp3",
    "video1.mp4",
    "book1.epub",
    "font1.ttf",
    "unknown.xyz",
]

def main() -> None:
    TEST_DIR.mkdir(exist_ok=True)

    for file_name in FILES:
        file_path = TEST_DIR / file_name
        file_path.touch(exist_ok=True)

    print("✅ Test files created successfully.")


if __name__ == "__main__":
    main()
