"""Input validation for order parameters."""
from __future__ import annotations

import re

from bot.exceptions import ValidationError

VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}
SYMBOL_PATTERN = re.compile(r"^[A-Z0-9]{5,20}$")


def validate_symbol(symbol: str) -> str:
    """Validate and normalize a trading symbol."""
    symbol = symbol.strip().upper()
    if not SYMBOL_PATTERN.match(symbol):
        raise ValidationError(f"Invalid symbol: '{symbol}'.")
    return symbol


def validate_side(side: str) -> str:
    """Validate order side."""
    side = side.strip().upper()
    if side not in VALID_SIDES:
        raise ValidationError(f"Invalid side: '{side}'. Must be one of {VALID_SIDES}.")
    return side


def validate_order_type(order_type: str) -> str:
    """Validate order type."""
    order_type = order_type.strip().upper()
    if order_type not in VALID_TYPES:
        raise ValidationError(
            f"Invalid order type: '{order_type}'. Must be one of {VALID_TYPES}."
        )
    return order_type


def validate_quantity(quantity: float) -> float:
    """Validate order quantity is a positive number."""
    if quantity is None or quantity <= 0:
        raise ValidationError(f"Quantity must be positive, got: {quantity}.")
    return float(quantity)


def validate_price(price: float | None, order_type: str) -> float | None:
    """Validate price is provided and positive for LIMIT orders."""
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValidationError("Price must be a positive number for LIMIT orders.")
        return float(price)
    return None
