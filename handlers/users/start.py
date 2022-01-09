from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Shunchaki menga qo'shiqchi yoki qo'shiq nomini jo'nating va men siz uchun musiqa topib beraman!\n"
                        f"/song - qo'shiq nomi orqali qidirish\n"
                        f"/artist - Qo'shiqchi ismi orqali qidirish\n"
                        f"/setlang - tilni sozlash\n"
                        f"/settings - sozlamalarni o'zgartirish")


@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    await message.answer("""🔥 Buyruqlar
Shunchaki menga qo'shiqchi yoki qo'shiq nomini jo'nating va men siz uchun musiqa topib beraman!
/song - qo'shiq nomi orqali qidirish
/artist - Qo'shiqchi ismi orqali qidirish
/my - sizning pleylistlaringiz ro'yhati
/top - mashhur qo'shiqlar
/settings - sozlamalarni o'zgartirish

Bog'lanish uchun aloqa: @kassir""")
