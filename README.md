# Binance Futures Testnet Trading Bot

A Python-based command-line application that places **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**. The application follows a modular architecture with input validation, structured logging, exception handling, and an enhanced interactive CLI.

---

## Features

- Place **Market** and **Limit** Orders
- Support for **BUY** and **SELL** orders
- Interactive **CLI Menu** (Bonus)
- Command-line argument support using `argparse`
- Input validation
- Logging of API requests, responses, and errors
- Exception handling
- Secure API credential management using `.env`

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .gitignore
├── README.md
├── requirements.txt
└── .env (Not included in GitHub)
```

---

## Technologies Used

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yash-1411/trading-bot-binance-testnet.git
cd trading-bot-binance-testnet
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

## Usage

### Interactive Menu (Bonus Feature)

Run:

```bash
python -m bot.cli
```

Menu:

```text
==========================================
      BINANCE FUTURES TESTNET BOT
==========================================

1. Show Account Information
2. Place Market Order
3. Place Limit Order
4. Exit
```

---

### View Account Information

```bash
python -m bot.cli --info
```

---

### Place a Market Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Place a Limit Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Logging

Application logs are stored in:

```text
logs/trading_bot.log
```

The log file records:

- Application startup
- API requests
- API responses
- Order placement
- Errors and exceptions

---

## Error Handling

The application handles:

- Invalid CLI inputs
- Invalid order parameters
- Binance API errors
- Network failures
- Configuration errors
- Unexpected exceptions

---

## Bonus Implemented

**Enhanced CLI User Experience**

Instead of requiring users to remember long command-line arguments, the application provides an interactive menu that allows users to:

- View account information
- Place Market orders
- Place Limit orders
- Exit the application

This improves usability while maintaining full CLI support.

---



---

## Author

**Yeshaswini M**

GitHub: https://github.com/yash-1411

---

## License

This project was developed as part of a Python Developer technical assessment.
