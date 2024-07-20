import requests
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ''

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
        'JPY_USD': round(usd_to_jpy, 2)  # 1달러 당 엔화 가치 계산, 소수점 2자리까지
    }
    return rates

async def send_exchange_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rates = get_exchange_rates()
    message = (
        f"Current exchange rates:\n"
        f"1 USD = {rates['USD_KRW']} KRW\n"
        f"1 CNY = {rates['CNY_KRW']} KRW\n"
        f"100 JPY = {rates['JPY_KRW100']} KRW\n"
        f"1 USD = {rates['JPY_USD']} JPY\n"
    )
    await update.message.reply_text(message)
    print(f"Sent message at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I will send you the current exchange rates now.')
    await send_exchange_rate(update, context)
    await update.message.reply_text('From now on, send me "dd" to get the current exchange rates.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == 'dd':
        await send_exchange_rate(update, context)
    else:
        await update.message.reply_text('Send me "dd" to get the current exchange rates.')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
