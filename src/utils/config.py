import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import warnings

load_dotenv()
warnings.filterwarnings("ignore")  # used due to warnings from whisper loading model

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Create work directory
WORK_DIR = Path.home() / "yt_summarizer_files"
WORK_DIR.mkdir(parents=True, exist_ok=True)