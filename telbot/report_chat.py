import asyncio
from datetime import datetime, timedelta
from telegram import Bot

# 텔레그램 봇의 토큰과 채팅 ID
TOKEN = '7237789333:AAEXcjHUjEN-M32fqLJM3B9vRpHn8lSUXi8'
CHAT_ID = '1751952106'

async def send_daily_report():
    bot = Bot(token=TOKEN)
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Daily report generated at {current_time}"
        
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("Daily report sent!")
        
        # 다음 실행 시간 계산 (매일 같은 시간에 실행되도록 설정)
        now = datetime.now()
        next_run = now.replace(hour=16, minute=5, second=0, microsecond=0)
        if now >= next_run:
            next_run += timedelta(days=1)
        sleep_duration = (next_run - now).total_seconds()
        
        await asyncio.sleep(sleep_duration)

async def main():
    await send_daily_report()

# 메인 이벤트 루프 실행
if __name__ == '__main__':
    asyncio.run(main())
