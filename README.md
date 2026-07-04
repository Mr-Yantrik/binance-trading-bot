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
python -m streamlit run ui/app.py
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





##  Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Mr-Yantrik/binance-trading-bot.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Copy the example file:

```bash
cp .env.example .env
```

Open `.env` and add your Binance Futures Testnet API credentials:

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_API_SECRET
```

### 5. Get Binance Testnet API Keys

1. Visit: https://testnet.binancefuture.com
2. Log in to your Binance Futures Testnet account.
3. Create API Keys.
4. Copy the API Key and Secret Key into the `.env` file.

### 6. Run the CLI

Market Order:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Limit Order:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

### 7. Run the Streamlit UI

```bash
python -m streamlit run ui/app.py
```

Open the URL shown in the terminal (usually):

```
http://localhost:8501
```

### 8. Run Unit Tests

```bash
pytest
```

### 9. Log Files

The application automatically creates log files containing API requests, responses, and errors.

### 10. Notes

- This application works only with Binance Futures Testnet.
- Never commit your `.env` file.
- Keep your API Secret private.

