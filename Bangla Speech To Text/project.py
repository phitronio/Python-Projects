import tkinter as tk
import speech_recognition as sr
import pyperclip

def copyText():
    text = T.get('1.0', tk.END)
    pyperclip.copy(text)
    
def voiceCommand():
    recognizer = sr.Recognizer()
    voice_btn.config(text='Listening...', bg='steelblue', fg='white')
    
    with sr.Microphone() as source:
        root.update()
        
        try:
            audio = recognizer.listen(source, timeout=1)
            text = recognizer.recognize_google(audio, language='bn-BD')
            T.insert(tk.END , text+" ")
            output_label.config(text="Completed")
        except sr.UnknownValueError:
            output_label.config(text="Not Understand")
        except sr.RequestError:
            output_label.config(text="Request Error")
        finally:
            voice_btn.config(text="Voice", bg="lightgreen", fg="black")
            
    

root = tk.Tk()
root.title("Bangla Speech to Text")

T = tk.Text(root)
T.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.TOP, fill=tk.X)

copy_btn = tk.Button(btn_frame, text="Copy text", bg="white", fg="black", width=20, height=2, command=copyText)
copy_btn.pack(side=tk.TOP, padx=10, pady=10)

voice_btn = tk.Button(btn_frame, text="Voice", bg="lightgreen", fg="black", width=20, height=2, command=voiceCommand )
voice_btn.pack(side=tk.TOP, padx=10, pady=10)

output_label = tk.Label(root, text="Output label")
output_label.pack(side=tk.BOTTOM)

tk.mainloop()

