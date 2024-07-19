import asyncio
from telegram import Bot

# 텔레그램 봇의 토큰과 채팅 ID
TOKEN = '7237789333:AAEXcjHUjEN-M32fqLJM3B9vRpHn8lSUXi8'
CHAT_ID = '1751952106'

# 비동기 함수 정의
async def send_message():
    bot = Bot(token=TOKEN)
    try:
        # 메시지 보내기
        await bot.send_message(chat_id=CHAT_ID, text="hello")
        print("Message sent!")
    except Exception as e:
        print(f"An error occurred: {e}")

# 비동기 함수 실행
asyncio.run(send_message())
