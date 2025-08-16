# src/bot/data/ohlcv.py
from ..exchanges.bitget import connect_bitget
from ccxt.base.errors import NetworkError, ExchangeError

ex = connect_bitget()

def fetch_ohlcv(symbol: str, timeframe: str = "15m", limit: int = 200):
    """
    Bitget 무기한 선물(symbol 예: 'BTC/USDT:USDT')의 OHLCV를 반환.
    반환 형식: [ [ms, open, high, low, close, volume], ... ]
    """
    for _ in range(3):  # 네트워크 일시 오류 대비 3회 재시도
        try:
            ex.load_markets()
            return ex.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        except (NetworkError, ExchangeError) as e:
            last = e
    raise last
