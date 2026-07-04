"""Centralized logging configuration with colorized console output."""
from __future__ import annotations

import logging
import sys

from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

_LEVEL_COLORS = {
    logging.DEBUG: Fore.CYAN,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,
}


class ColorFormatter(logging.Formatter):
    """Formatter that colorizes log level names for console output."""

    def format(self, record: logging.LogRecord) -> str:
        color = _LEVEL_COLORS.get(record.levelno, "")
        record.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"
        return super().format(record)


def setup_logging(log_file: str = "bot.log", level: str = "INFO") -> logging.Logger:
    """Configure and return the root application logger."""
    logger = logging.getLogger("binance_bot")
    logger.setLevel(level)
    logger.propagate = False

    if logger.handlers:
        return logger

    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(ColorFormatter(fmt, datefmt))
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(fmt, datefmt))
    logger.addHandler(file_handler)

    return logger
