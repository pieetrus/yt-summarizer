from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

class YouTubeTranscriptExtractor:
    @staticmethod
    def extract_transcript(video_id):
        try:
            srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            transcript_text = ' '.join([entry['text'] for entry in srt])
            print("Transcript downloaded successfully.")
            return transcript_text
        except (NoTranscriptFound, TranscriptsDisabled):
            print("Transcript not available from YouTube.")
            return None