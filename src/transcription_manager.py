import yt_dlp

from src.audio.audio_downloader import AudioDownloader
from src.audio.whisper_transcriber import WhisperTranscriber
from src.transcript.transcript_formatter import TranscriptFormatter
from src.transcript.transcript_saver import TranscriptSaver
from src.transcript.youtube_transcript_extractor import YouTubeTranscriptExtractor
from src.utils.config import WORK_DIR


class TranscriptionManager:
    def __init__(self, language):
        self.downloader = AudioDownloader()
        self.transcriber = WhisperTranscriber(language)
        self.formatter = TranscriptFormatter()
        self.saver = TranscriptSaver()
        self.youtube_extractor = YouTubeTranscriptExtractor()

    def process_video(self, video_url):
        video_id = video_url.split("v=")[-1]

        # Try to get YouTube transcript first
        transcript = self.youtube_extractor.extract_transcript(video_id)

        if transcript is None:
            print("Falling back to audio transcription...")
            audio_path, video_title = self.downloader.download(video_url)
            transcript = self.transcriber.transcribe(audio_path)
        else:
            # If YouTube transcript is available, we still need to get the video title
            with yt_dlp.YoutubeDL(self.downloader.ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)
                video_title = info['title']
        # Save the transcript
        sanitized_title = self.sanitize_filename(video_title)
        transcript_filename = f"{sanitized_title}_transcript.txt"
        transcript_path = WORK_DIR / transcript_filename
        self.saver.save_transcript(transcript, str(transcript_path))

        return transcript, video_title
    
    @staticmethod
    def sanitize_filename(filename):
        return "".join([c for c in filename if c.isalpha() or c.isdigit() or c in ' -_.']).rstrip()
