import os

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set")
