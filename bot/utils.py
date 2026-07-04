"""Shared utility helpers for output formatting."""
from __future__ import annotations

from typing import Any

from colorama import Fore, Style


def format_order_result(order: dict[str, Any]) -> str:
    """Format an order response into a human-readable summary."""
    lines = [
        f"{Fore.CYAN}{Style.BRIGHT}Order Summary{Style.RESET_ALL}",
        f"  Order ID   : {order.get('orderId')}",
        f"  Symbol     : {order.get('symbol')}",
        f"  Side       : {order.get('side')}",
        f"  Type       : {order.get('type')}",
        f"  Quantity   : {order.get('origQty')}",
        f"  Price      : {order.get('price')}",
        f"  Status     : {order.get('status')}",
    ]
    return "\n".join(lines)


def print_success(message: str) -> None:
    """Print a success message in green."""
    print(f"{Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print an error message in red."""
    print(f"{Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}")
