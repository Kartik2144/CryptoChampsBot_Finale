from datetime import datetime
import pytz

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_signal(signal):
    if signal.get("no_trade"):
        msg = "📭 No ultra-strong setups found today."
    else:
        msg = (
    f"🚀 CryptoChamps Signal ({signal['strategy']})\n\n"
    f"🔹 Pair: {signal['pair']}\n"
    f"📍 Direction: {signal['direction']} (20x)\n"
    f"🎯 Entry: {signal['entry']}\n"
    f"⛔ Stoploss: {signal['sl']}\n"
    f"✅ Target: {signal['tp']}\n"
    f"📈 Risk-Reward: 1:1.5\n"
    f"🤖 Confidence: {signal['confidence']}%\n\n"
    f"#{signal['pair'].split('/')[0]} #{signal['strategy'].replace('-', '')} #{signal['direction']}"
)

    print(msg)  # ✅ Replace with Telegram API send

def send_daily_pnl():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    print(f"📊 Daily PnL Summary for {now.strftime('%d %B %Y')}\n✅ TP Hits: 2 | ❌ SL Hits: 0\n💰 Simulated PnL: +8.5% (20x)")
