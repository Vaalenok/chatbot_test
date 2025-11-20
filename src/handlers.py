from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import src.db.crud as crud
import src.db.models as models
import src.functions as functions
from src.openai import get_response


router = Router()


@router.message(Command("start"))
async def start(msg: Message):
    user = await crud.get_by_param(models.User, tg_id=msg.from_user.id)

    if user:
        user.message_history.clear()
        await crud.update(user)
        await msg.answer("Контекст сброшен!")
    else:
        user = models.User(tg_id=msg.from_user.id)
        await crud.create(user)
        await msg.answer(
            "Привет! Я - твой личный ассистент. Задай мне какой-нибудь вопрос"
        )


@router.message(Command("help"))
async def _help(msg: Message):
    await msg.answer(
        "Я - твой личный ассистент. Ты можешь сбросить контекст диалога командой /start"
    )


@router.message(F.text & ~F.text.startswith("/"))
async def message(msg: Message):
    user = await crud.get_by_param(models.User, tg_id=msg.from_user.id)

    if not user:
        return

    sent_msg = await msg.answer("Генерирую ответ...")

    message_to_model = functions.form_message(user, msg.text)
    response, sliced = get_response(message_to_model)
    user.message_history.append(
        models.Message(author=models.Author.USER, content=msg.text)
    )
    user.message_history.append(
        models.Message(author=models.Author.ASSISTANT, content=response)
    )

    if sliced:
        user.message_history = user.message_history[sliced * 2 :]

    await crud.update(user)
    await sent_msg.edit_text(response)
