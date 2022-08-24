import asyncio
from aiogram import Bot, Dispatcher, types
from db.repository import SqlRepository

sqlRepository = SqlRepository()


async def start_handler(event: types.Message):
    if not sqlRepository.is_user_exist(event.from_user.id):
        sqlRepository.save_user(event.from_user.id, event.from_user.username)
    await event.answer(
        f"Suck some dick, {event.from_user.get_mention(as_html=True)}",
        parse_mode=types.ParseMode.HTML,
    )


async def main():
    bot = Bot(token='5424635298:AAFD7j_hdpcSigqeAL5i1XnpKOdf-xQMMlk')
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()


asyncio.run(main())
