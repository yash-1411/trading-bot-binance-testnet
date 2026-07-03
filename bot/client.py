import time
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import get_logger

logger = get_logger(__name__)


class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret

       

        try:
            self.client = Client(api_key, api_secret, testnet=testnet)

            # Sync with Binance server time
            server_time = self.client.get_server_time()
            self.client.timestamp_offset = (
                server_time["serverTime"] - int(time.time() * 1000)
            )

            

            logger.info(f"Binance Futures client initialized (testnet={testnet}")

        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise

    def get_account_info(self):
        try:
            account_info = self.client.futures_account()
            logger.info(
                f"Account info retrieved: {account_info.get('totalAccountEquity', 'N/A')} USDT"
            )
            return account_info

        except BinanceAPIException as e:
            logger.error(f"API Error getting account info: {e}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Network error getting account info: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error getting account info: {e}")
            raise

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
                recvWindow=10000
            )

            logger.info(f"MARKET order placed successfully: {order.get('orderId')}")
            logger.debug(f"Order response: {order}")

            return order

        except Exception as e:
            logger.error(f"API Error placing market order: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price,
                recvWindow=10000
            )

            logger.info(f"LIMIT order placed successfully: {order.get('orderId')}")
            logger.debug(f"Order response: {order}")

            return order

        except Exception as e:
            logger.error(f"API Error placing limit order: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None):
        if order_type == "MARKET":
            return self.place_market_order(symbol, side, quantity)

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")

            return self.place_limit_order(symbol, side, quantity, price)

        raise ValueError(f"Unsupported order type: {order_type}")