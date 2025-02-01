import structlog
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


from core.constants import REGISTER_HANDLER_CALLBACK_DATA


logger = structlog.getLogger(__file__)
router = Router()

@router.callback_query(F.data == REGISTER_HANDLER_CALLBACK_DATA)
async def cmd_register_handler(
    callback: CallbackQuery,
    state: FSMContext,
) -> None:
    # await state.set_state(RegisterHandler)
    await callback.message.answer('Введите своё имя')
