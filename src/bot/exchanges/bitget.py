# before
# from bot import config

# after
from .. import config  # bot 패키지 기준 상대 import로 변경
import ccxt
from .. import config   # ✅ 상대 import

def connect_bitget():
    exchange = ccxt.bitget({
        "apiKey": config.EXCHANGE_API_KEY,
        "secret": config.EXCHANGE_API_SECRET,
        "password": config.EXCHANGE_PASSWORD,
        "enableRateLimit": True,
        "options": {"defaultType": "swap"},
    })
    return exchange
