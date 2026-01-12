# Smart File Organizer (CLI)

### Project Summary

**Smart File Organizer (CLI)** is a Python command-line tool designed to automatically organize files in any directory into categorized folders based on their file extensions. This project demonstrates:

- **Real-world automation:** Recursively organizes files from subfolders, safe for freelance or personal automation tasks.
- **Duplicate handling:** Avoids overwriting by renaming duplicates (e.g., `report.pdf`, `report_1.pdf`).
- **Dry-run mode:** Preview file movements before actually moving them, ensuring safety.
- **Extensible architecture:** File categories are configurable via `config.py`, making it easy to add new types.
- **Logging:** All operations are tracked in a log file for transparency and debugging.
- **Clean CLI experience:** Minimal prompts, interactive dry-run, and simple input for directory paths.

**Project Milestones:**

1. Initial Setup: Created project structure, CLI entry point (`main.py`), and basic organizer logic.
2. File Categorization: Implemented extension-based categorization with configurable categories.
3. Dry-Run Feature: Added simulation mode to preview file movements without affecting original files.
4. Duplicate File Handling: Introduced automatic renaming for duplicate files to prevent overwriting.
5. Finalization: Added logging, recursive file discovery, README documentation, and pushed the final version to GitHub.

**Outcome:**  
A safe, professional, and extensible Python CLI tool for organizing files, suitable for personal use, portfolio demonstration, or freelance automation projects.

---

## Features

- Recursively organizes files from all subfolders.
- Categorizes files such as Documents, Images, Audio, Videos, Ebooks, Fonts, and Others.
- Automatically creates folders if they do not exist.
- Prevents overwriting by renaming duplicates (e.g., `report.pdf`, `report_1.pdf`).
- Safe file movement with logging of all operations.
- Supports **dry-run mode** to simulate actions without moving files.
- Works with any directory path provided by the user.
- Configuration-driven categories via `config.py`.
- Designed for CLI use and future enhancements like undo.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ykhan-dev/smart-file-organizer.git
cd smart-file-organizer
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

_Currently, this project uses only the Python standard library._

---

## Usage

Run the organizer:

```bash
python main.py
```

You will be prompted to **enter the directory path** you want to organize and whether you want to run in dry-run mode:

```
Enter directory to organize: /path/to/your/folder
Dry-run mode? (y/n): y
```

- **Dry-run mode (`y`)**: Shows what files would be moved without actually moving them.
- **Normal mode (`n`)**: Moves files into categorized folders.

### Example Dry-Run Output with Duplicate Handling

```
[DRY-RUN] Would move 'a/report.pdf' to 'Documents/report.pdf'
[DRY-RUN] Would move 'b/report.pdf' to 'Documents/report_1.pdf'
[DRY-RUN] Would move 'a/photo.jpg' to 'Images/photo.jpg'
[DRY-RUN] Would move 'b/photo.jpg' to 'Images/photo_1.jpg'
✅ Dry-run complete. No files were moved.
```

### Example Folder After Real Run

```
test_folder/
├── Audio/
│   ├── song1.mp3
│   └── song2.wav
├── Documents/
│   ├── report.pdf
│   └── report_1.pdf
├── Images/
│   ├── photo.jpg
│   └── photo_1.jpg
├── Videos/
│   ├── video1.mp4
│   └── video2.mov
├── Ebooks/
│   └── ebook1.epub
├── Fonts/
│   └── font1.ttf
└── Others/
    └── unknown.xyz
```

---

## Project Structure

smart-file-organizer/
├── main.py
├── organizer/
│ ├── organizer.py
│ ├── config.py
│ ├── utils.py
│ └── logger.py
└── README.md

- `main.py` — CLI entry point that handles user input, validation, and dry-run.
- `organizer/organizer.py` — Core logic for file categorization, movement, duplicate handling, and dry-run.
- `organizer/config.py` — File category configuration.
- `organizer/utils.py` — Utility functions (e.g., ensure folders exist).
- `organizer/logger.py` — Logging setup for tracking file operations.

---

## File Categories

Files are organized based on extensions defined in `config.py`:

- **Documents:** pdf, docx, txt, xlsx, pptx, csv, etc.
- **Images:** jpg, jpeg, png, gif, bmp, tiff, svg, webp, heic
- **Audio:** mp3, wav, aac, flac, ogg, m4a, wma
- **Videos:** mp4, mov, avi, mkv, flv, wmv, webm, mpeg
- **Ebooks:** epub, mobi, azw3
- **Fonts:** ttf, otf, woff, woff2
- **Others:** Any unknown or uncategorized file types

---

## Future Enhancements

- Undo last operation.
- Additional CLI arguments for non-interactive use.
- Further extension of file categories and rules.

---

## License

This project is licensed under the MIT License.
