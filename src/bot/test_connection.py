# src/bot/test_connection.py
from .exchanges.bitget import connect_bitget

def main():
    ex = connect_bitget()
    print("→ loading markets...")
    ex.load_markets()
    print("✔ markets loaded. symbols:", len(ex.symbols))

    print("→ fetching balance...")
    bal = ex.fetch_balance()
    usdt = bal.get("USDT", {})
    print("✔ USDT balance:", {
        "total": usdt.get("total"),
        "free": usdt.get("free"),
        "used": usdt.get("used"),
    })

if __name__ == "__main__":
    main()

# src/bot/test_connection.py
from .exchanges.bitget import connect_bitget
from .data.ohlcv import fetch_ohlcv
from . import config
from .indicators.ema import ema

def main():
    ex = connect_bitget()
    print("→ loading markets...")
    ex.load_markets()
    print("✔ markets loaded. symbols:", len(ex.symbols))

    print("→ fetching balance...")
    bal = ex.fetch_balance()
    usdt = bal.get("USDT", {})
    print("✔ USDT balance:", {"total": usdt.get("total"), "free": usdt.get("free"), "used": usdt.get("used")})

    # === OHLCV & EMA 테스트 ===
    symbol = config.SYMBOLS[0] if isinstance(config.SYMBOLS, list) else "BTC/USDT:USDT"
    tf = config.TIMEFRAME if hasattr(config, "TIMEFRAME") else "15m"
    print(f"→ fetching OHLCV: {symbol} {tf}")
    candles = fetch_ohlcv(symbol, tf, limit=200)
    closes = [c[4] for c in candles]

    ema_fast = ema(closes, 9)
    ema_slow = ema(closes, 21)

    last_close = closes[-1]
    last_fast = ema_fast[-1]
    last_slow = ema_slow[-1]
    signal = "LONG" if last_fast > last_slow else "SHORT"

    print("✔ last close:", last_close)
    print("✔ EMA9 / EMA21:", round(last_fast, 4), "/", round(last_slow, 4))
    print("✔ Signal:", signal)

if __name__ == "__main__":
    main()

# ... (네가 이미 작성한 코드 아래에 붙이기)
from .execution.trade import ensure_leverage, market_order, fetch_positions

    # === (선택) 주문/포지션 스켈레톤 테스트 ===
    symbol = symbol  # 위에서 사용한 심볼 재사용
    print("→ ensure leverage (cross 5x)")
    ensure_leverage(symbol, leverage=5, margin_mode="cross")

    print("→ positions (before):")
    print(fetch_positions(symbol))

    # 아주 소량 모의 주문 예 (DRY_RUN=True라 체결 안 됨)
    print("→ dry-run market buy 0.001 (contract amount 예시)")
    market_order(symbol, "buy", amount=0.001)

    print("→ positions (after):")
    print(fetch_positions(symbol))
