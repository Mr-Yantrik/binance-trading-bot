"""Order placement logic for Binance Futures Testnet."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from binance import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.exceptions import OrderExecutionError
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

logger = logging.getLogger("binance_bot")


@dataclass(frozen=True)
class OrderRequest:
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: float | None = None


def build_order_request(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
) -> OrderRequest:
    """Validate raw inputs and build a normalized OrderRequest."""
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)
    return OrderRequest(symbol, side, order_type, quantity, price)


class OrderService:
    """Encapsulates order execution against the Binance Futures client."""

    def __init__(self, client: Client) -> None:
        self._client = client

    def place_order(self, request: OrderRequest) -> dict[str, Any]:
        """Submit an order to Binance Futures Testnet."""
        params: dict[str, Any] = {
            "symbol": request.symbol,
            "side": request.side,
            "type": request.order_type,
            "quantity": request.quantity,
        }

        if request.order_type == "LIMIT":
            params["price"] = request.price
            params["timeInForce"] = "GTC"

        logger.info(
            "Placing %s %s order: symbol=%s qty=%s price=%s",
            request.order_type,
            request.side,
            request.symbol,
            request.quantity,
            request.price,
        )

        try:
            response = self._client.futures_create_order(**params)
            logger.info("Order executed successfully: orderId=%s", response.get("orderId"))
            return response
        except (BinanceAPIException, BinanceRequestException) as exc:
            logger.error("Order execution failed: %s", exc)
            raise OrderExecutionError(f"Order failed: {exc}") from exc
        except Exception as exc:  # noqa: BLE001
            logger.error("Unexpected error during order execution: %s", exc)
            raise OrderExecutionError(f"Unexpected order error: {exc}") from exc
