from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from src.config import TG_BOT_TOKEN


bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()


commands = [
    BotCommand(command="start", description="Сбросить контекст"),
    BotCommand(command="help", description="Помощь"),
]


async def start_polling():
    from src.handlers import router

    dp.include_router(router)

    await bot.set_my_commands(commands)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
