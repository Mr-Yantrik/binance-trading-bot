"""Application configuration loaded from environment."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

from bot.exceptions import ConfigError

load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    api_secret: str
    testnet_base_url: str = "https://testnet.binancefuture.com"
    recv_window: int = 5000
    log_level: str = "INFO"
    log_file: str = "bot.log"


def load_settings() -> Settings:
    """Load and validate settings from environment variables."""
    api_key = os.getenv("API_KEY", "").strip()
    api_secret = os.getenv("API_SECRET", "").strip()

    if not api_key or not api_secret:
        raise ConfigError("API_KEY and API_SECRET must be set in environment (.env).")

    return Settings(
        api_key=api_key,
        api_secret=api_secret,
        log_level=os.getenv("LOG_LEVEL", "INFO").strip().upper(),
        log_file=os.getenv("LOG_FILE", "bot.log").strip(),
    )
