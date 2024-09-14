import yt_dlp
from pathlib import Path

from src.utils.config import WORK_DIR


class AudioDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': str(WORK_DIR / '%(title)s.%(ext)s'),
        }

    def download(self, video_url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([video_url])
            info = ydl.extract_info(video_url, download=False)
            filename = ydl.prepare_filename(info)
            return Path(filename).with_suffix('.mp3'), info['title']