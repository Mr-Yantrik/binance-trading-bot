"""Unit tests for bot.orders."""
from unittest.mock import MagicMock

import pytest
from binance.exceptions import BinanceAPIException

from bot.exceptions import OrderExecutionError, ValidationError
from bot.orders import OrderService, build_order_request


def test_build_order_request_market():
    req = build_order_request("btcusdt", "buy", "market", 1.0)
    assert req.symbol == "BTCUSDT"
    assert req.side == "BUY"
    assert req.order_type == "MARKET"
    assert req.price is None


def test_build_order_request_limit_requires_price():
    with pytest.raises(ValidationError):
        build_order_request("BTCUSDT", "SELL", "LIMIT", 1.0)


def test_place_order_success():
    mock_client = MagicMock()
    mock_client.futures_create_order.return_value = {"orderId": 123, "status": "FILLED"}
    service = OrderService(mock_client)
    request = build_order_request("BTCUSDT", "BUY", "MARKET", 1.0)

    result = service.place_order(request)

    assert result["orderId"] == 123
    mock_client.futures_create_order.assert_called_once()


def test_place_order_limit_includes_price_and_tif():
    mock_client = MagicMock()
    mock_client.futures_create_order.return_value = {"orderId": 1}
    service = OrderService(mock_client)
    request = build_order_request("BTCUSDT", "SELL", "LIMIT", 1.0, 50000.0)

    service.place_order(request)

    _, kwargs = mock_client.futures_create_order.call_args
    assert kwargs["price"] == 50000.0
    assert kwargs["timeInForce"] == "GTC"


def test_place_order_api_exception_raises_order_execution_error():
    mock_client = MagicMock()
    mock_response = MagicMock(status_code=400, text='{"code":-1121}')
    mock_client.futures_create_order.side_effect = BinanceAPIException(
        mock_response, 400, mock_response.text
    )
    service = OrderService(mock_client)
    request = build_order_request("BTCUSDT", "BUY", "MARKET", 1.0)

    with pytest.raises(OrderExecutionError):
        service.place_order(request)
