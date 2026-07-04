"""Streamlit UI for the Binance Futures Testnet trading bot."""
from __future__ import annotations

import streamlit as st

from bot.client import create_client
from bot.config import load_settings
from bot.exceptions import BotError
from bot.logging_config import setup_logging
from bot.orders import OrderService, build_order_request

st.set_page_config(page_title="Binance Futures Testnet Bot", page_icon="📈", layout="centered")


@st.cache_resource
def get_order_service() -> OrderService:
    settings = load_settings()
    setup_logging(settings.log_file, settings.log_level)
    client = create_client(settings)
    return OrderService(client)


def main() -> None:
    st.title("📈 Binance Futures Testnet Trading Bot")
    st.caption("Place MARKET or LIMIT orders on Binance Futures Testnet.")

    with st.form("order_form"):
        symbol = st.text_input("Symbol", value="BTCUSDT").upper()
        side = st.selectbox("Side", ["BUY", "SELL"])
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        quantity = st.number_input("Quantity", min_value=0.0, step=0.001, format="%.6f")
        price = None
        if order_type == "LIMIT":
            price = st.number_input("Price", min_value=0.0, step=0.01, format="%.2f")
        submitted = st.form_submit_button("Place Order")

    if submitted:
        try:
            service = get_order_service()
            request = build_order_request(symbol, side, order_type, quantity, price)
            with st.spinner("Submitting order..."):
                result = service.place_order(request)
            st.success(f"Order placed successfully. Order ID: {result.get('orderId')}")
            st.json(result)
        except BotError as exc:
            st.error(str(exc))
        except Exception as exc:  # noqa: BLE001
            st.error(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()
