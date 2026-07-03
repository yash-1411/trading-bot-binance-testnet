from bot.logging_config import get_logger

logger = get_logger(__name__)

class OrderResponse:
    @staticmethod
    def format_order_summary(symbol, side, order_type, quantity, price=None):
        price_str = f" @ {price}" if price else ""
        return f"\n{'='*60}\nORDER SUMMARY\n{'='*60}\nSymbol:      {symbol}\nSide:        {side}\nType:        {order_type}{price_str}\nQuantity:    {quantity}\n{'='*60}\n"
    
    @staticmethod
    def format_order_response(order):
        order_id = order.get('orderId', 'N/A')
        status = order.get('status', 'N/A')
        executed_qty = order.get('executedQty', '0')
        avg_price = order.get('avgPrice', 'N/A')
        return f"\n{'='*60}\nORDER RESPONSE\n{'='*60}\nOrder ID:    {order_id}\nStatus:      {status}\nExecuted Qty: {executed_qty}\nAvg Price:   {avg_price}\n{'='*60}\n"
    
    @staticmethod
    def print_success(order):
        order_id = order.get('orderId', 'N/A')
        status = order.get('status', 'N/A')
        logger.info(f"Order placed successfully! ID: {order_id}, Status: {status}")
        print(f"\nSUCCESS! Order placed successfully.")
        print(f"  Order ID: {order_id}")
        print(f"  Status: {status}\n")
    
    @staticmethod
    def print_failure(error):
        logger.error(f"Order failed: {error}")
        print(f"\nFAILED! Order could not be placed.")
        print(f"  Error: {error}\n")
    
    @staticmethod
    def display_order_result(symbol, side, order_type, quantity, price=None, order=None, error=None):
        print(OrderResponse.format_order_summary(symbol, side, order_type, quantity, price))
        if order:
            print(OrderResponse.format_order_response(order))
            OrderResponse.print_success(order)
        elif error:
            OrderResponse.print_failure(error)
        else:
            print("No response received from exchange.")
