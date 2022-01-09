from aiogram import types

from loader import dp


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