from loguru import logger
from .config import settings

def run():
    logger.info(f"Starting bot on {settings.EXCHANGE} symbols={settings.SYMBOLS} tf={settings.TIMEFRAME}")
    # TODO: 데이터 수집 → 지표계산 → 시그널 → 주문

if __name__ == "__main__":
    run()
