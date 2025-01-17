import asyncio 
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES 

lang_values = list(LANGUAGES.values())
lang_key = list(LANGUAGES.keys())

async def translate():
    try:
        txt = text1.get(1.0, tk.END).strip()
        
        c1 = combo.get()
        
        if txt:
            pos = lang_values.index(c1)
            c1_code = lang_key[pos]
            
            translator = Translator()
            result =  await translator.translate(txt, dest=c1_code)
            
            text2.delete(1.0, tk.END)
            text2.insert(1.0, result.text)
            
            
        else :
            messagebox.showwarning("Input Error", "Please enter some text to translate!")
    
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = tk.Tk()
root.title("Language Translator Tool")
root.minsize(700, 600)
root.resizable(False, False)

root.option_add("*TCombobox*Listbox.font", ("normal", 15))
root.option_add("*TCombobox.font", ("normal",15))

text1 = tk.Text(root, font=('normal', 15), padx=10,pady=10)
text1.place(width=600, height=200, x=50, y=50)

combo = ttk.Combobox(root, values=lang_values, state='readonly')
combo.place(x=50, y=280)
combo.set("Choose a language")

button = tk.Button(root, text="Translate", font=("normal", 15), bg="lightgreen", command=lambda:asyncio.run(translate()))
button.place(x=310, y=270)

text2 = tk.Text(root, font=('normal', 15), padx=10,pady=10)
text2.place(width=600, height=200, x=50, y=350)

root.mainloop()
