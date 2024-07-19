import asyncio
import requests
from datetime import datetime, time
from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '7237789333:AAEXcjHUjEN-M32fqLJM3B9vRpHn8lSUXi8'
CHAT_ID = '1751952106'

def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    usd_to_krw = data['rates']['KRW']
    usd_to_cny = data['rates']['CNY']
    usd_to_jpy = data['rates']['JPY']
    
    rates = {
        'USD_KRW': round(usd_to_krw),
        'CNY_KRW': round(usd_to_krw / usd_to_cny),
        'JPY_KRW100': round((usd_to_krw / usd_to_jpy) * 100),  # 100엔 당 원화 가치 계산
        'JPY_USD': round(usd_to_jpy) # 1엔 당 달러 가치 계산
    }
    return rates

async def send_exchange_rate(context: ContextTypes.DEFAULT_TYPE):
    rates = get_exchange_rates()
    message = (
        f"Current exchange rates:\n"
        f"1 USD = {rates['USD_KRW']} KRW\n"
        f"1 CNY = {rates['CNY_KRW']} KRW\n"
        f"100 JPY = {rates['JPY_KRW100']} KRW\n"
        f"1 JPY = {rates['JPY_USD']} USD\n"
    )
    await context.bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Sent message at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

async def start(update: ContextTypes.DEFAULT_TYPE, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I will send you the exchange rates now and every morning at 7:30 AM.')
    await send_exchange_rate(context)

async def setup_daily_job(application: Application):
    await send_exchange_rate(application)  # 즉시 한 번 실행
    application.job_queue.run_daily(send_exchange_rate, time=time(hour=7, minute=30))

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    
    # 봇 시작 시 즉시 메시지를 보내고 일일 작업 설정
    application.job_queue.run_once(setup_daily_job, when=1)

    # 봇 실행
    application.run_polling()

if __name__ == '__main__':
    main()