from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_keyboard(product):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data=f"product:{product}"),
        ],
    ])
    return keys
