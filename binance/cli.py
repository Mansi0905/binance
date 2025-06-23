def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Order Type (MARKET/LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None
    if order_type == 'LIMIT':
        price = float(input("Limit Price: "))
    return symbol, side, order_type, quantity, price
