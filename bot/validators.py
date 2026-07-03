import re
from bot.logging_config import get_logger

logger = get_logger(__name__)

class ValidationError(Exception):
    pass

def validate_symbol(symbol):
    if not symbol:
        raise ValidationError("Symbol cannot be empty")
    symbol = symbol.upper().strip()
    if not re.match(r'^[A-Z0-9]+$', symbol):
        raise ValidationError(f"Invalid symbol format: {symbol}")
    if len(symbol) < 3 or len(symbol) > 10:
        raise ValidationError(f"Symbol length must be between 3 and 10 characters")
    logger.debug(f"Symbol validated: {symbol}")
    return symbol

def validate_side(side):
    if not side:
        raise ValidationError("Side cannot be empty")
    side = side.upper().strip()
    if side not in ['BUY', 'SELL']:
        raise ValidationError(f"Invalid side: {side}. Must be 'BUY' or 'SELL'")
    logger.debug(f"Side validated: {side}")
    return side

def validate_order_type(order_type):
    if not order_type:
        raise ValidationError("Order type cannot be empty")
    order_type = order_type.upper().strip()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValidationError(f"Invalid order type: {order_type}")
    logger.debug(f"Order type validated: {order_type}")
    return order_type

def validate_quantity(quantity):
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValidationError(f"Quantity must be positive")
        if qty > 1000000:
            raise ValidationError(f"Quantity too large")
        logger.debug(f"Quantity validated: {qty}")
        return qty
    except ValueError:
        raise ValidationError(f"Invalid quantity: {quantity}")

def validate_price(price):
    try:
        price_val = float(price)
        if price_val <= 0:
            raise ValidationError(f"Price must be positive")
        logger.debug(f"Price validated: {price_val}")
        return price_val
    except ValueError:
        raise ValidationError(f"Invalid price: {price}")

def validate_order_params(symbol, side, order_type, quantity, price=None):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    
    if order_type == 'LIMIT':
        if not price:
            raise ValidationError("Price is required for LIMIT orders")
        price = validate_price(price)
    elif price:
        logger.warning("Price provided for MARKET order (will be ignored)")
        price = None
    
    logger.info(f"Order parameters validated: {symbol} {side} {order_type} qty={quantity}")
    return symbol, side, order_type, quantity, price or 0.0
