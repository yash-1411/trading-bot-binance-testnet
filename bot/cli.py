
import argparse
import sys
import os
from dotenv import load_dotenv
load_dotenv() 
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import setup_logging, get_logger
from bot.client import BinanceFuturesClient
from bot.orders import OrderResponse
from bot.validators import validate_order_params, ValidationError

logger = get_logger()

def load_credentials():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    if not api_key or not api_secret:
        raise ValueError("API credentials not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables or create a .env file.")
    return api_key, api_secret

def interactive_mode():
    print("\n" + "="*60)
    print("BINANCE FUTURES TESTNET TRADING BOT")
    print("="*60 + "\n")
    
    try:
        api_key, api_secret = load_credentials()
        client = BinanceFuturesClient(api_key, api_secret, testnet=True)
        
        try:
            account_info = client.get_account_info()
            print(f"Connected to Binance Futures Testnet")
            print(f"  Account Balance: {account_info.get('totalAccountEquity', 'N/A')} USDT\n")
        except Exception as e:
            print(f"Warning: Could not retrieve account info: {e}\n")
        
        print("Enter order details:\n")
        symbol = input("Symbol (e.g., BTCUSDT): ").strip()
        side = input("Side (BUY/SELL): ").strip()
        order_type = input("Order Type (MARKET/LIMIT): ").strip()
        quantity = input("Quantity: ").strip()
        
        price = None
        if order_type.upper() == 'LIMIT':
            price = input("Price: ").strip()
        
        try:
            symbol, side, order_type, quantity, price = validate_order_params(symbol, side, order_type, quantity, price)
        except ValidationError as e:
            print(f"\nValidation Error: {e}")
            sys.exit(1)
        
        try:
            order = client.place_order(symbol, side, order_type, quantity, price)
            OrderResponse.display_order_result(symbol, side, order_type, quantity, price, order=order)
        except Exception as e:
            OrderResponse.display_order_result(symbol, side, order_type, quantity, price, error=e)
            sys.exit(1)
        
    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        logger.exception("Unexpected error in interactive mode")
        sys.exit(1)

def cli_mode():
    parser = argparse.ArgumentParser(description='Binance Futures Testnet Trading Bot')
    parser.add_argument('--symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', type=str, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--type', type=str, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', type=str, help='Order quantity')
    parser.add_argument('--price', type=str, help='Order price (required for LIMIT orders)')
    parser.add_argument('--info', action='store_true', help='Show account information')
    parser.add_argument('--log-level', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    parser.add_argument('--log-file', type=str, default='logs/trading_bot.log')
    
    args = parser.parse_args()
    setup_logging(args.log_level, args.log_file)
    logger.info("CLI mode started")
    
    try:
        api_key, api_secret = load_credentials()
        client = BinanceFuturesClient(api_key, api_secret, testnet=True)
        
        if args.info:
            try:
                account_info = client.get_account_info()
                print(f"\nAccount Information:")
                print(f"  Total Balance: {account_info.get('totalAccountEquity', 'N/A')} USDT")
                print(f"  Available Balance: {account_info.get('availableBalance', 'N/A')} USDT")
                print(f"  Initial Margin: {account_info.get('totalInitialMargin', 'N/A')} USDT")
                print(f"  Maint Margin: {account_info.get('totalMaintMargin', 'N/A')} USDT")
                print(f"  Unrealized PnL: {account_info.get('totalUnrealizedProfit', 'N/A')} USDT")
                print(f"  Margin Balance: {account_info.get('marginBalance', 'N/A')} USDT")
                print()
                return
            except Exception as e:
                print(f"\nError retrieving account info: {e}")
                sys.exit(1)
        
        if not all([args.symbol, args.side, args.type, args.quantity]):
            parser.error("--symbol, --side, --type, and --quantity are required")
        
        try:
            symbol, side, order_type, quantity, price = validate_order_params(args.symbol, args.side, args.type, args.quantity, args.price)
        except ValidationError as e:
            print(f"\nValidation Error: {e}")
            sys.exit(1)
        
        try:
            order = client.place_order(symbol, side, order_type, quantity, price)
            OrderResponse.display_order_result(symbol, side, order_type, quantity, price, order=order)
        except Exception as e:
            OrderResponse.display_order_result(symbol, side, order_type, quantity, price, error=e)
            sys.exit(1)
        
    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        logger.exception("Unexpected error in CLI mode")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        cli_mode()

if __name__ == "__main__":
    main()
