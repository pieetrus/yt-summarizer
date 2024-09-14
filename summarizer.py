
import re
import time
from pathlib import Path

import librosa
import whisper
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

class AudioDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',
        }

    def download(self, video_url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([video_url])
            info = ydl.extract_info(video_url, download=False)
            filename = ydl.prepare_filename(info)
            return Path(filename).with_suffix('.mp3')

class WhisperTranscriber:
    def __init__(self, model_name="base.en"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        start_time = time.time()
        result = self.model.transcribe(str(audio_path))
        end_time = time.time()
        
        duration = librosa.get_duration(filename=str(audio_path))
        transcription_time = end_time - start_time
        
        print(f"Video length: {duration:.2f} seconds")
        print(f"Transcription time: {transcription_time:.2f} seconds")
        
        return result["text"]

class TranscriptFormatter:
    @staticmethod
    def format_transcript(text):
        sentences = re.split("([!?.])", text)
        sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
        return "\n\n".join(sentences)

class TranscriptSaver:
    @staticmethod
    def save_transcript(transcript, file_path):
        output_path = file_path.with_suffix('.txt')
        with open(output_path, "w") as f:
            f.write(transcript)
        print(f"\n\n{'-'*100}\n\nYour transcript is here: {output_path}")

class YouTubeTranscriptExtractor:
    @staticmethod
    def extract_transcript(video_id):
        try:
            srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            with open("subtitles.txt", "w") as f:
                for i in srt:
                    f.write(f"{i}\n")
            print("Transcript downloaded successfully.")
        except NoTranscriptFound:
            print("Transcript in text format was not found")
            return False
        return True

class TranscriptionManager:
    def __init__(self):
        self.downloader = AudioDownloader()
        self.transcriber = WhisperTranscriber()
        self.formatter = TranscriptFormatter()
        self.saver = TranscriptSaver()
        self.youtube_extractor = YouTubeTranscriptExtractor()

    def process_video(self, video_url):
        video_id = video_url.split("v=")[-1]
        
        if not self.youtube_extractor.extract_transcript(video_id):
            print("Falling back to audio transcription...")
            audio_path = self.downloader.download(video_url)
            raw_transcript = self.transcriber.transcribe(audio_path)
            formatted_transcript = self.formatter.format_transcript(raw_transcript)
            self.saver.save_transcript(formatted_transcript, audio_path)

def main():
    print("Welcome to the video summarizer!")
    print("So far only english language videos are supported.\n")
    video_url = input("Enter a YouTube video URL: ")
    manager = TranscriptionManager()
    manager.process_video(video_url)

if __name__ == "__main__":
    main()