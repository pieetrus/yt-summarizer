from src.openai.chat import chat
from src.transcription_manager import TranscriptionManager
from src.utils.config import WORK_DIR

def main():
    print("Welcome to the video summarizer!\n")
    print("For now there is only support for English and Polish language!\n")
    print("In order to start you need to provide YouTube video url and language in iso code!\n")
    
    video_url = input("Enter a YouTube video URL: ")
    video_language = input("Enter a YouTube video language (iso-code, ie. 'en', 'pl'): ")
    summary_language = input("Enter a summarization language (iso-code, ie. 'en', 'pl'): ")

    manager = TranscriptionManager(video_language)
    transcript, video_title = manager.process_video(video_url)

    if transcript:
        print("\nVideo processed! Now wait for summary.\n")

        system_msg = 'You are a helpful assistant who wants to summarize me a video transcript.'
        user_msg = 'Summarize the video transcript that I sent you. Write me key points in bullet points.'

        chat_response = chat(system_msg, [user_msg, transcript], summary_language)

        sanitized_title = TranscriptionManager.sanitize_filename(video_title)
        output_filename = f"{sanitized_title}_summary.md"
        output_path = WORK_DIR / output_filename

        with open(output_path, "w", encoding='utf-8') as f:
            f.write(chat_response)

    else:
        print("Failed to process the video. Please try again.")

if __name__ == "__main__":
    main()