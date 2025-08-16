# src/bot/indicators/ema.py
def ema(values, period):
    k = 2 / (period + 1)
    ema_val = None
    out = []
    for v in values:
        if ema_val is None:
            ema_val = v
        else:
            ema_val = v * k + ema_val * (1 - k)
        out.append(ema_val)
    return out
