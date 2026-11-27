import pytest
from telegram import Update
from bot.handlers import start

@pytest.mark.asyncio
async def test_start_command():
    # ساخت شبیه‌سازی از Update و Context
    update = MockUpdate()
    context = MockContext()
    
    await start.start_command(update, context)
    
    # بررسی اینکه پیام ارسال شده است
    assert update.message.reply_text.called
