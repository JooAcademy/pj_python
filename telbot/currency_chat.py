import asyncio
import requests
from datetime import datetime, time
from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = ''
CHAT_ID = ''

def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    rates = {
        'KRW': data['rates']['KRW'],
        'CNY': data['rates']['CNY'],
        'JPY': data['rates']['JPY']
    }
    return rates

async def send_exchange_rate(context: ContextTypes.DEFAULT_TYPE):
    rates = get_exchange_rates()
    message = (
        f"Here are the current exchange rates (USD to):\n"
        f"KRW: {rates['KRW']}\n"
        f"CNY: {rates['CNY']}\n"
        f"JPY: {rates['JPY']}"
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
