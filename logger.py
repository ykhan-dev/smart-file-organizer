"""
logger.py

Centralized logging configuration for the application.
All file operations are logged for safety and debugging.
"""

import logging
from pathlib import Path

# Directory where logs will be stored
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Configure logging format and file
logging.basicConfig(
    filename=LOG_DIR / "organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger() -> logging.Logger:
    """
    Return a configured logger instance.

    Returns:
        logging.Logger: Logger for the Smart File Organizer.
    """
    return logging.getLogger("SmartFileOrganizer")
