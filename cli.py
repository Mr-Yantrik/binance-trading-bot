"""Enhanced CLI for the Binance Futures Testnet trading bot."""
from __future__ import annotations

import argparse
import sys

from bot.client import create_client
from bot.config import load_settings
from bot.exceptions import BotError
from bot.logging_config import setup_logging
from bot.orders import OrderService, build_order_request
from bot.utils import format_order_result, print_error, print_success


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="Binance Futures Testnet Trading Bot CLI",
    )
    parser.add_argument("-s", "--symbol", required=True, help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument(
        "-side", "--side", required=True, choices=["BUY", "SELL"], help="Order side"
    )
    parser.add_argument(
        "-t", "--type", required=True, choices=["MARKET", "LIMIT"], dest="order_type",
        help="Order type",
    )
    parser.add_argument("-q", "--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument(
        "-p", "--price", type=float, default=None, help="Order price (required for LIMIT)"
    )
    parser.add_argument(
        "--log-level", default=None, help="Override log level (DEBUG, INFO, WARNING, ERROR)"
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    """Run the CLI. Returns process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        settings = load_settings()
        logger = setup_logging(settings.log_file, args.log_level or settings.log_level)

        request = build_order_request(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price,
        )

        client = create_client(settings)
        service = OrderService(client)
        result = service.place_order(request)

        print_success("Order placed successfully.")
        print(format_order_result(result))
        return 0

    except BotError as exc:
        print_error(f"Error: {exc}")
        return 1
    except Exception as exc:  # noqa: BLE001
        print_error(f"Unexpected error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(run())
