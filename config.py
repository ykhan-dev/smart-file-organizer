"""
config.py

This module contains configuration data for the Smart File Organizer.
It defines how files are categorized based on their file extensions.

Keeping this separate makes the project:
- Easy to customize
- Safer to modify
- AI-ready in the future
"""


FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ods",
        ".ppt", ".pptx", ".odp", ".md", ".csv"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"
    ],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Scripts": [
        ".py", ".js", ".ts", ".sh", ".bat", ".ps1", ".rb", ".php", ".pl", ".java",
        ".c", ".cpp", ".cs"
    ],
    "Ebooks": [".epub", ".mobi", ".azw3"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Others": []  # Catch-all category for unknown extensions
}
