import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
from pydub import AudioSegment
import os

def audio_to_text(audio_file, language):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Use the selected language for speech recognition
        if language == "English":
            text = recognizer.recognize_google(audio, language="en-US")
        elif language == "Spanish":
            text = recognizer.recognize_google(audio, language="es-AR")
        else:
            text = "Unsupported language"

        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

def open_file():
    # Open a file dialog to select an audio file
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.ogg")])

    if file_path:
        # Convert .ogg to .wav
        wav_file_path = file_path[:-4] + ".wav"
        convert_ogg_to_wav(file_path, wav_file_path)

        # Convert audio to text
        language = language_var.get()
        text = audio_to_text(wav_file_path, language)
        result_label.config(text="Text from audio:\n" + text)

        # Clean up temporary .wav file
        os.remove(wav_file_path)

def convert_ogg_to_wav(ogg_file, wav_file):
    ogg_audio = AudioSegment.from_file(ogg_file, format="ogg")
    ogg_audio.export(wav_file, format="wav")

# Create the GUI window
window = tk.Tk()
window.title("Audio to Text")
window.geometry("400x400")

# Create a frame to hold the label and make it expand to fill the window
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Create a label to display the result
result_label = tk.Label(frame, text="", wraplength=350, justify=tk.LEFT)
result_label.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

# Create a language selection dropdown menu
language_var = tk.StringVar()
language_var.set("Spanish")  # Default selection
language_menu = tk.OptionMenu(window, language_var, "English", "Spanish")
language_menu.pack(pady=10)

# Create a button to open the file dialog
button = tk.Button(window, text="Select Audio File", command=open_file)
button.pack(ipadx=10, ipady=12, pady=20)

# Start the GUI event loop
window.mainloop()
