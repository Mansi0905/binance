from config import API_KEY, API_SECRET

print("DEBUG API_KEY:", API_KEY)
print("DEBUG API_SECRET:", API_SECRET)


from config import API_KEY, API_SECRET
from bot import BasicBot
from cli import get_user_input
from logger import setup_logger

setup_logger()

bot = BasicBot(API_KEY, API_SECRET)

symbol, side, order_type, quantity, price = get_user_input()
order = bot.place_order(symbol, side, order_type, quantity, price)

if order:
    print("✅ Order placed successfully!")
    print(order)
else:
    print("❌ Order failed.")
print("API_KEY:", API_KEY)
print("API_SECRET:", API_SECRET)
