import whisper
from pydub import AudioSegment
import openai
import os

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def process_audio(file_path):
    """Converts audio to wav if necessary and loads it."""
    filename, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.mp3':
        print(f"Converting {file_path} to wav...")
        audio = AudioSegment.from_mp3(file_path)
        wav_path = filename + ".wav"
        audio.export(wav_path, format="wav")
        return wav_path
    return file_path

def transcribe_audio(file_path):
    """Transcribes audio using OpenAI Whisper (Local)."""
    print("Loading Whisper model...")
    # 'base' is fast; use 'small', 'medium', or 'large' for better accuracy
    model = whisper.load_model("base")
    
    print("Transcribing...")
    result = model.transcribe(file_path)
    return result['text']

def summarize_text(text):
    """Summarizes the transcription using GPT-4."""
    print("Summarizing content...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes audio transcripts clearly and concisely."},
            {"role": "user", "content": f"Please summarize the following transcript:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content

def main(audio_input):
    try:
        # 1. Pre-process
        ready_audio = process_audio(audio_input)
        
        # 2. Transcribe
        transcript = transcribe_audio(ready_audio)
        print("\n--- Full Transcript ---")
        print(transcript)
        
        # 3. Summarize
        summary = summarize_text(transcript)
        print("\n--- Summary ---")
        print(summary)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_to_process = "your_audio_file.mp3" # Replace with your file path
    main(file_to_process)
