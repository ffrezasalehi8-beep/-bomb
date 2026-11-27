from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.config import Config
from bot.handlers import start, help_command, admin, download, convert, fun
import logging

# تنظیم لاگ‌گیری
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    Config.validate()
    
    # ساخت اپلیکیشن
    application = Application.builder().token(Config.BOT_TOKEN).build()
    
    # ثبت دستورات
    application.add_handler(CommandHandler("start", start.start_command))
    application.add_handler(CommandHandler("help", help_command.help_command))
    application.add_handler(CommandHandler("admin", admin.admin_panel))
    
    # دستورات دانلود
    application.add_handler(CommandHandler("download", download.download_command))
    
    # دستورات تبدیل
    application.add_handler(CommandHandler("to_pdf", convert.to_pdf_command))
    
    # دستورات سرگرمی
    application.add_handler(CommandHandler("joke", fun.joke_command))
    application.add_handler(CommandHandler("fortune", fun.fortune_command))
    
    # مدیریت پیام‌های متنی (برای پردازش لینک‌ها)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download.handle_text))
    
    # اجرای ربات
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
