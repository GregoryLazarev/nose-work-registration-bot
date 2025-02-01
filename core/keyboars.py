from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from core.constants import (
    REGISTER_HANDLER_CALLBACK_DATA,
    REGISTER_K9_CALLBACK_DATA,
)


register_keyboard_buttons = [
    [
        InlineKeyboardButton(
            text='Зарегистрировать проводника',
            callback_data=REGISTER_HANDLER_CALLBACK_DATA,
        )
    ],
    [
        InlineKeyboardButton(
            text='Зарегистрировать собаку',
            callback_data=REGISTER_K9_CALLBACK_DATA,
        )
    ],
]
register_keyboard = InlineKeyboardMarkup(inline_keyboard=register_keyboard_buttons)
