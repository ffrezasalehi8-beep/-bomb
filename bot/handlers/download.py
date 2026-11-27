from telegram import Update
from telegram.ext import ContextTypes
from bot.services.youtube import download_youtube_video
import os

async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لطفاً لینک را وارد کنید: /download <url>")
        return
    
    url = context.args[0]
    await update.message.reply_text("⏳ در حال دانلود...")
    
    try:
        file_path = await download_youtube_video(url)
        with open(file_path, 'rb') as video:
            await update.message.reply_video(video)
        os.remove(file_path)  # پاک کردن فایل موقت
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {str(e)}")
