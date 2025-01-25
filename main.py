import json
import os
from typing import Any

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import (
    default_handler_router,
    register_handler_router,
)


async def handler(
    event: dict[str, Any],
    context: str,
) -> dict[str, Any]:
    bot = Bot(
        token=os.environ.get('TG_TOKEN'),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    try:
        dp.include_router(default_handler_router)
        dp.include_router(register_handler_router)
    except RuntimeError as e:
        if 'Router is already attached to' in str(e):
            pass
        else:
            raise e

    messages = event.get('messages', [])
    for message in messages:
        details = message.get('details', {})
        event_message = details.get('message', {})
        raw_update_str = event_message.get('body', '')
        raw_update = json.loads(raw_update_str)

        await dp.feed_raw_update(
            bot=bot,
            update=raw_update,
        )
    return {'statusCode': 200, 'body': 'ok'}
