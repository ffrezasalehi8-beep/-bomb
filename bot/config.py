import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bot.db")
    ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    WIKIPEDIA_API_URL = os.getenv("WIKIPEDIA_API_URL")
    REDIS_URL = os.getenv("REDIS_URL")
    
    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is not set!")
