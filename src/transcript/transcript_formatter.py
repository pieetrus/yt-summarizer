import re

class TranscriptFormatter:
    @staticmethod
    def format_transcript(text):
        sentences = re.split("([!?.])", text)
        sentences = ["".join(i) for i in zip(sentences[0::2], sentences[1::2])]
        return "\n\n".join(sentences)