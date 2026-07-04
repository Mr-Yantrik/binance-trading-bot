# Binance Futures Testnet Trading Bot

CLI and Streamlit trading bot for Binance USDT-M Futures Testnet. Supports MARKET and LIMIT, BUY and SELL orders.

## Features

- CLI order placement with validation and structured logging
- Streamlit web UI
- Colorized console output
- Custom exception hierarchy
- Unit tests (pytest)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set your Binance Futures Testnet API credentials:

```
API_KEY=...
API_SECRET=...
```

Get testnet credentials at https://testnet.binancefuture.com

## CLI Usage

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

Arguments:

| Flag | Required | Description |
|---|---|---|
| `-s, --symbol` | yes | Trading pair, e.g. BTCUSDT |
| `-side, --side` | yes | BUY or SELL |
| `-t, --type` | yes | MARKET or LIMIT |
| `-q, --quantity` | yes | Order quantity |
| `-p, --price` | LIMIT only | Order price |
| `--log-level` | no | Override log level |

## Streamlit UI

```bash
streamlit run ui/app.py
```

## Tests

```bash
pytest
```

## Project Structure

```
bot/
  config.py
  client.py
  orders.py
  validators.py
  logging_config.py
  exceptions.py
  utils.py
ui/
  app.py
tests/
  test_validators.py
  test_orders.py
cli.py
```

## Disclaimer

Testnet only. No real funds are involved. Use at your own risk.
