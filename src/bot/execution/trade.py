# src/bot/execution/trade.py
from ..exchanges.bitget import connect_bitget
from .. import config

# 안전장치: 기본은 모의모드(DRY_RUN=True). 실주문하려면 False로.
DRY_RUN = True

ex = connect_bitget()

def ensure_leverage(symbol: str, leverage: int = 5, margin_mode: str = "cross"):
    """
    Bitget 무기한 선물 레버리지/증거금 모드 설정.
    margin_mode: "cross" | "isolated"
    """
    params = {"marginMode": margin_mode}
    try:
        # ccxt 표준: set_leverage(exchange, leverage, symbol, params)
        ex.set_leverage(leverage, symbol, params)
    except Exception as e:
        print(f"[warn] set_leverage failed: {e}")

def market_order(symbol: str, side: str, amount: float, reduce_only: bool = False):
    """
    단순 시장가 주문. amount는 계약 수(컨트랙트 수) 기준.
    Bitget(선물)의 수량 단위는 시장/심볼마다 다를 수 있어, 소량 테스트 권장.
    """
    params = {"reduceOnly": reduce_only}
    if DRY_RUN:
        print(f"[DRY_RUN] create_order: symbol={symbol}, side={side}, amount={amount}, type=market, params={params}")
        return {"id": "dryrun", "info": {"dry": True}}
    return ex.create_order(symbol, type="market", side=side, amount=amount, params=params)

def close_position_market(symbol: str, side_current: str, amount: float):
    """
    보유 포지션을 시장가로 청산 (reduceOnly=True).
    side_current: 현재 포지션 방향 ('long' 또는 'short')에 맞춰 반대 주문을 자동 수행.
    """
    side = "sell" if side_current == "long" else "buy"
    return market_order(symbol, side, amount, reduce_only=True)

def fetch_positions(symbol: str):
    """
    현재 포지션 정보 요약.
    """
    try:
        pos = ex.fetch_positions([symbol])
        return pos
    except Exception as e:
        print(f"[warn] fetch_positions error: {e}")
        return []
