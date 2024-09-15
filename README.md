# YouTube Video Summarizer

This project is a Python-based tool that downloads YouTube videos, transcribes them, and generates summaries using OpenAI's GPT model. It supports English and Polish language for both video transcription and summary generation.

## Features

- Download audio from YouTube videos
- Transcribe audio using OpenAI's Whisper model
- Extract existing YouTube transcripts when available
- Generate summaries using OpenAI's GPT model
- Support for English and Polish language in both transcription and summarization

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the main script:

```
python main.py
```

Follow the prompts to:
1. Enter a YouTube video URL
2. Specify the language of the video (for transcription)
3. Choose the language for the summary

The script will then:
- Download the audio from the YouTube video
- Transcribe the audio (or extract the existing transcript if available)
- Generate a summary in the specified language
- Save the transcript and summary in the work directory (default: `./yt_summarizer_files/`)