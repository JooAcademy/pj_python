import asyncio
from datetime import datetime, timedelta
from telegram import Bot

# 텔레그램 봇의 토큰과 채팅 ID
TOKEN = ''
CHAT_ID = ''

async def send_hourly_report():
    bot = Bot(token=TOKEN)
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Hourly report generated at {current_time}"
        
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("Hourly report sent!")
        
        # 1시간 대기
        await asyncio.sleep(3600)

async def main():
    await send_hourly_report()

# 메인 이벤트 루프 실행
if __name__ == '__main__':
    asyncio.run(main())

