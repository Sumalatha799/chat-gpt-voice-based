
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import webbrowser
import playsound

# Configure API key
api_data = "YOUR_API_KEY"
genai.configure(api_key=api_data)

# Initialize Gemini 1.5 model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get AI response and convert to audio
def reply_audio(question):
    response = model.generate_content(question)
    text_response = response.text

    # Convert response to speech
    tts = gTTS(text=text_response, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts.save(tmp_file.name)
        playsound.playsound(tmp_file.name)
        os.remove(tmp_file.name)

    return text_response

# Function to listen to user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}")
    except Exception:
        print("Could not understand. Please say that again.")
        return None
    return query.lower()

# Main loop
if __name__ == "__main__":
    while True:
        query = take_command()
        if query:
            if "open youtube" in query:
                webbrowser.open("https://www.youtube.com")
            elif "open google" in query:
                webbrowser.open("https://www.google.com")
            elif "bye" in query:
                print("Goodbye!")
                break
            else:
                reply_audio(query)


