# src/bot/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# coin-bot/.env 명시 로드
ROOT = Path(__file__).resolve().parents[2]  # coin-bot
load_dotenv(ROOT / ".env")

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY", "")
EXCHANGE_API_SECRET = os.getenv("EXCHANGE_API_SECRET", "")
EXCHANGE_PASSWORD = os.getenv("EXCHANGE_PASSWORD", "")

# (선택) 추가 설정도 같이
EXCHANGE  = os.getenv("EXCHANGE", "bitget")
SYMBOLS   = [s.strip() for s in os.getenv("SYMBOLS", "BTC/USDT:USDT").split(",")]
TIMEFRAME = os.getenv("TIMEFRAME", "15m")
