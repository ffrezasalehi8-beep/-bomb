import yt_dlp
import asyncio

async def download_youtube_video(url: str) -> str:
    """دانلود ویدیو از یوتیوب و برگرداندن مسیر فایل"""
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }
    
    loop = asyncio.get_event_loop()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = await loop.run_in_executor(None, ydl.extract_info, url)
        filename = ydl.prepare_filename(info)
        return filename
