# Binance Futures Testnet Trading Bot

A Python-based command-line trading bot that places **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**. The application is built with a modular architecture, input validation, structured logging, and robust exception handling.

---

## Features

- Place **Market** and **Limit** orders
- Supports **BUY** and **SELL** orders
- Command Line Interface (CLI) using `argparse`
- Input validation for all parameters
- Structured logging of API requests, responses, and errors
- Exception handling for invalid input, API errors, and network failures
- Secure API credential management using a `.env` file

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py             # Binance API client
│   ├── cli.py                # Command-line interface
│   ├── logging_config.py     # Logging configuration
│   ├── orders.py             # Order response handling
│   └── validators.py         # Input validation
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.9+
- Binance Futures Testnet account
- Binance Testnet API Key and Secret

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yash-1411/trading-bot-binance-testnet.git
cd trading-bot-binance-testnet
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Usage

### View Account Information

```bash
python -m bot.cli --info
```

### Place a Market Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Sample Output

```
============================================================
ORDER SUMMARY
============================================================
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

============================================================
ORDER RESPONSE
============================================================
Order ID: 18768348061
Status: NEW
Executed Qty: 0.0000

SUCCESS! Order placed successfully.
```

---

## Logging

All API requests, responses, and errors are recorded in:

```
logs/trading_bot.log
```

---

## Error Handling

The application handles:

- Invalid user input
- Missing configuration
- Binance API errors
- Network failures
- Unexpected exceptions

---

## Technologies Used

- Python
- python-binance
- argparse
- python-dotenv
- logging

---


---

## Author

**Yeshaswini M**

GitHub: https://github.com/yash-1411

---

## License

This project was developed as part of a Python Developer technical assessment.
