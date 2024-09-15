import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import warnings

load_dotenv()
warnings.filterwarnings("ignore")  # used due to warnings from whisper loading model

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Get the directory of the main.py script
MAIN_DIR = Path(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# Create work directory
WORK_DIR = MAIN_DIR / "yt_summarizer_files"
WORK_DIR.mkdir(parents=True, exist_ok=True)