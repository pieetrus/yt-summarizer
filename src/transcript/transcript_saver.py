from pathlib import Path

class TranscriptSaver:
    @staticmethod
    def save_transcript(transcript, file_path):
        output_path = Path(file_path)
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(transcript)
        print(f"\n\n{'-'*100}\n\nYour transcript is here: {output_path}")