#@title Полный код бота для самоконтроля
import asyncio
import logging

from QuizData import quiz_data
from DBfuncs import get_quiz_index
from GlobalObjects import DP, BOT
import QuizLogic

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
from DBfuncs import create_table

# Запуск процесса поллинга новых апдейтов
async def main():
    await create_table()
    await DP.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(main())