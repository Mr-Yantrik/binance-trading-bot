"""Unit tests for bot.validators."""
import pytest

from bot.exceptions import ValidationError
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)


def test_validate_symbol_valid():
    assert validate_symbol("btcusdt") == "BTCUSDT"


def test_validate_symbol_invalid():
    with pytest.raises(ValidationError):
        validate_symbol("BT")


def test_validate_side_valid():
    assert validate_side("buy") == "BUY"


def test_validate_side_invalid():
    with pytest.raises(ValidationError):
        validate_side("HOLD")


def test_validate_order_type_valid():
    assert validate_order_type("market") == "MARKET"


def test_validate_order_type_invalid():
    with pytest.raises(ValidationError):
        validate_order_type("STOP_LIMIT")


def test_validate_quantity_valid():
    assert validate_quantity(1.5) == 1.5


@pytest.mark.parametrize("qty", [0, -1, None])
def test_validate_quantity_invalid(qty):
    with pytest.raises(ValidationError):
        validate_quantity(qty)


def test_validate_price_limit_valid():
    assert validate_price(100.0, "LIMIT") == 100.0


def test_validate_price_limit_invalid():
    with pytest.raises(ValidationError):
        validate_price(None, "LIMIT")


def test_validate_price_market_ignored():
    assert validate_price(None, "MARKET") is None
