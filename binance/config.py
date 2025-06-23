import os
from dotenv import load_dotenv

print("Loading .env...")
load_dotenv(".env")  # load variables from .env file

print("Current dir:", os.getcwd())

API_KEY = os.getenv("bf73cd01d292e81b2107164bef3391e63ef36418451ca32c495ab03ed437d2c1")      # pass ENV VAR NAME, NOT actual key string
API_SECRET = os.getenv("83c5dc920c978010e0843fed5a6526e336447414b08cea85cc001593e3cbdee8")

print("From config.py:", API_KEY, API_SECRET)
