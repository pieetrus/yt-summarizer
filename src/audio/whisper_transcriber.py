import time
import whisper
import librosa

class WhisperTranscriber:
    def __init__(self, language, model_name="base"):
        self.model = whisper.load_model(model_name)
        self.language = language

    def transcribe(self, audio_path):
        start_time = time.time()
        print("Transcribing audio...\n")
        result = self.model.transcribe(str(audio_path), language=self.language, fp16=False, verbose=False)
        print("Audio transcribed!")
        end_time = time.time()

        duration = librosa.get_duration(filename=str(audio_path))
        transcription_time = end_time - start_time

        print(f"Video length: {duration:.2f} seconds")
        print(f"Transcription time: {transcription_time:.2f} seconds")

        return result["text"]