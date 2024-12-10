from tkinter import *
from tkinter import ttk
import threading
import requests

root = Tk()

root.geometry("700x700")
root.title("AI Chatbot")
# Dark theme colors
background_color = "#2C3E50"  
text_color = "#D3D3D3"        
button_color = "#FFA07A"      
enter_bg_color = "#34495E"    
enter_text_color = "#FFFFFF"  

root.configure(background=background_color)

question_var = StringVar()

progressbar = ttk.Progressbar(root, mode="indeterminate")

def start_progress():
    progressbar.start()

def stop_progress():
    progressbar.stop()

def fetch_answer():
        print("Generating Answer...")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAsX29Tx_fYsklapse_jwRe2msFpaiD7e8"
        question = question_var.get()

        # Prepare payload for the API
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": question}
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)

        data = response.json()
        answer = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "No response received.")
        

        text_box.delete("1.0", END)
        text_box.insert(END, answer)
        stop_progress()

def generate_answer():
    threading.Thread(target=start_progress).start()
    threading.Thread(target=fetch_answer).start()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_box = Text(root, height=30, width=0, font=('Microsoft YaHei Light', 14, "bold"),yscrollcommand=scrollbar.set, bg=enter_bg_color, fg=text_color, insertbackground=text_color)
text_box.pack(pady=10, fill=BOTH, expand=True)

scrollbar.config(command=text_box.yview)

question_label = Label(root, text="Enter your question:", font=('Microsoft YaHei Light', 14, "bold"),bg=background_color, fg=text_color)
question_label.pack(pady=5)

question_entry = Entry( root, textvariable=question_var, font=('Microsoft YaHei Light', 14, "bold"),bg=enter_bg_color, fg=enter_text_color, insertbackground=enter_text_color)
question_entry.pack(pady=5)

ask_button = Button(root, text="Generate Response", command=generate_answer,font=("Microsoft YaHei Light", 14, "bold"), bg=button_color, fg=text_color)
ask_button.pack(pady=10)

progressbar.pack(pady=10)

root.mainloop()
