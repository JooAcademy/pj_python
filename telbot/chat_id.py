


from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
# 텔레그램 봇 토큰 입력
TOKEN = ''

async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Your chat ID is: {chat_id}')

def main() -> None:
    # Application 객체 생성
    application = Application.builder().token(TOKEN).build()

    # 핸들러 등록
    application.add_handler(CommandHandler("start", start))

    # 봇 시작
    application.run_polling()

if __name__ == '__main__':
    main()
