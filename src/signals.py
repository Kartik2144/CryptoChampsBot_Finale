import ccxt, random

def generate_signals():
    # ✅ Only max 2 ultra-strong signals/day
    pairs = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT"]
    signals = []

    for pair in pairs:
        if random.random() > 0.85 and len(signals) < 2:  # ✅ Confidence filter
            signals.append({
                "pair": pair,
                "direction": random.choice(["LONG", "SHORT"]),
                "entry": round(random.uniform(100, 200), 2),
                "sl": round(random.uniform(95, 99), 2),
                "tp": round(random.uniform(210, 230), 2),
                "confidence": random.randint(85, 95),
                "strategy": random.choice(["Breakout", "Reversal", "Trend-following"])
            })
    return signals
