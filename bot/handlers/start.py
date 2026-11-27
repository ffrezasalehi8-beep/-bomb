from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.models.user import User

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # ثبت کاربر در دیتابیس
    await User.get_or_create(
        telegram_id=user.id,
        defaults={"username": user.username, "first_name": user.first_name}
    )
    
    keyboard = [
        [InlineKeyboardButton("📚 راهنما", callback_data="help")],
        [InlineKeyboardButton("🎯 امکانات", callback_data="features")],
        [InlineKeyboardButton("👥 گروه ما", url="https://t.me/your_group")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"سلام {user.first_name}! 👋\n"
        "به ربات ما خوش آمدید. از دستور /help برای مشاهده راهنما استفاده کنید.",
        reply_markup=reply_markup
    )
