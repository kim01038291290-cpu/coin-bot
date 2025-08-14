from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    EXCHANGE: str = "bybit"
    EXCHANGE_API_KEY: str | None = None
    EXCHANGE_API_SECRET: str | None = None
    EXCHANGE_PASSWORD: str | None = None
    SYMBOLS: List[str] = ["BTC/USDT:USDT"]
    TIMEFRAME: str = "15m"

    class Config:
        env_file = ".env"

settings = Settings()
