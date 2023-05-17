import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr

def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Use the default Google Web Speech API to convert audio to text
        # recognize_google(audio, language="fr-FR")
        text = recognizer.recognize_google(audio, language="es-AR")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

def open_file():
    # Open a file dialog to select an audio file
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])

    # Convert audio to text
    if file_path:
        text = audio_to_text(file_path)
        result_label.config(text="Text from audio: " + text)

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

# Create a button to open the file dialog
button = tk.Button(window, text="Select Audio File", command=open_file)
button.pack(ipadx=10, ipady=12, pady=20)

# Start the GUI event loop
window.mainloop()