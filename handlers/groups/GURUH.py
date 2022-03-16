from aiogram import types
from aiogram.types import ContentType

from filters.Gr_bilan import Guruh2
from loader import dp


# Echo bot
@dp.message_handler(Guruh2(),content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    username = message.new_chat_members[0].username
    await message.delete()
    await message.answer(text=f'Guruhga xush kelibsiz {username}')


@dp.message_handler(Guruh2(),content_types=ContentType.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    username = message.left_chat_member.username
    await message.delete()
    await message.answer(text=f'Foyadalanuvchi guruhni tark etdi {username}')