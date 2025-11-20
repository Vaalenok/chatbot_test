import logging
from colorlog import ColoredFormatter
from src.db.database import engine, Base
from src.bot import start_polling
import asyncio


handler = logging.StreamHandler()
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    tasks = [init_db(), start_polling()]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        logging.info("Парсер запущен")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Парсер остановлен")

# TODO: редактировать readme
# TODO: docker-compose
# TODO: покрыть тестами
