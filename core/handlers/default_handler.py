import structlog
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from core.constants import WELCOME_MESSAGE
import keyboards as kb


logger = structlog.getLogger(__file__)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    logger.debug(
        'Got start message command',
        msg=message,
    )
    await message.answer(WELCOME_MESSAGE, reply_markup=kb.register_keyboard)
