from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 텔레그램 봇의 API 토큰 입력
TOKEN = '7237789333:AAEXcjHUjEN-M32fqLJM3B9vRpHn8lSUXi8'

# /start 명령어에 대한 핸들러 함수
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="환영합니다! 저는 파이썬 텔레봇입니다.")

# 메시지 핸들링을 위한 함수
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Updater 객체 생성
    updater = Updater(token=TOKEN, use_context=True)

    # Dispatcher 객체
    dispatcher = updater.dispatcher

    # /start 명령어에 대한 핸들러 추가
    dispatcher.add_handler(CommandHandler('start', start))

    # 모든 메시지에 대한 핸들러 추가
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 봇 시작
    updater.start_polling()

    # 종료 시그널을 받을 때까지 대기
    updater.idle()

if __name__ == '__main__':
    main()
