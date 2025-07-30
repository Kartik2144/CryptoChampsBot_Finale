import schedule, time
from src.signals import generate_signals
from src.telegram_bot import send_signal, send_daily_pnl

def job():
    signals = generate_signals()
    if signals:
        for s in signals:
            send_signal(s)
    else:
        send_signal({"no_trade": True})

schedule.every(20).minutes.do(job)
schedule.every().day.at("23:59").do(send_daily_pnl)

print("🚀 CryptoChampsBot Final is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
