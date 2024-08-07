import tkinter as tk
import pyttsx3

def convert_text_to_speech():
    text = text_entry.get("1.0", tk.END)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Text to Speech Converter")

# Create a text entry widget for input
text_entry = tk.Text(root, height=10, width=40)
text_entry.pack(padx=20, pady=20)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_text_to_speech)
convert_button.pack(pady=10)

root.mainloop()
