"""Binance Futures Testnet client factory."""
from __future__ import annotations

import logging

from binance import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import Settings
from bot.exceptions import ClientConnectionError

logger = logging.getLogger("binance_bot")


def create_client(settings: Settings) -> Client:
    """Create and validate a Binance Futures Testnet client."""
    try:
        client = Client(settings.api_key, settings.api_secret, testnet=True)
        client.FUTURES_URL = settings.testnet_base_url + "/fapi"
        client.futures_ping()
        logger.info("Connected to Binance Futures Testnet.")
        return client
    except (BinanceAPIException, BinanceRequestException) as exc:
        raise ClientConnectionError(f"Failed to connect to Binance Testnet: {exc}") from exc
    except Exception as exc:  # noqa: BLE001
        raise ClientConnectionError(f"Unexpected client initialization error: {exc}") from exc
