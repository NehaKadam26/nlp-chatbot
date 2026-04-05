import tkinter as tk
from tkinter import scrolledtext
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chatbot import get_response

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_box.config(state=tk.NORMAL)

    chat_box.insert(tk.END, "  You  \n", "user_tag")
    chat_box.insert(tk.END, f"  {user_input}\n\n", "user_msg")

    response = get_response(user_input)
    chat_box.insert(tk.END, "  🎓 Bot  \n", "bot_tag")
    chat_box.insert(tk.END, f"  {response}\n\n", "bot_msg")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)
    entry.delete(0, tk.END)

# --- Window ---
root = tk.Tk()
root.title("College Helpdesk Chatbot")
root.geometry("520x680")
root.resizable(False, False)
root.configure(bg="#f5f7ff")

# --- Header ---
header = tk.Frame(root, bg="#4a90d9", pady=14)
header.pack(fill=tk.X)

tk.Label(header, text="🎓 College Helpdesk Chatbot",
         font=("Helvetica", 16, "bold"),
         bg="#4a90d9", fg="white").pack()

tk.Label(header, text="Ask me about admissions, fees, courses & more",
         font=("Helvetica", 9),
         bg="#4a90d9", fg="#d0e8ff").pack()

# --- Chat Area ---
chat_frame = tk.Frame(root, bg="#f5f7ff")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

chat_box = scrolledtext.ScrolledText(
    chat_frame, state=tk.DISABLED, wrap=tk.WORD,
    font=("Helvetica", 11), bg="#ffffff", fg="#222222",
    relief=tk.FLAT, padx=10, pady=10, bd=0
)
chat_box.pack(fill=tk.BOTH, expand=True)

# Tags
chat_box.tag_config("user_tag", foreground="#1a73e8",
                    font=("Helvetica", 9, "bold"), spacing1=6)
chat_box.tag_config("user_msg", foreground="#003580",
                    font=("Helvetica", 11), lmargin1=10, lmargin2=10,
                    background="#dceeff", spacing3=4)
chat_box.tag_config("bot_tag", foreground="#2e7d32",
                    font=("Helvetica", 9, "bold"), spacing1=6)
chat_box.tag_config("bot_msg", foreground="#1b1b1b",
                    font=("Helvetica", 11), lmargin1=10, lmargin2=10,
                    background="#e8f5e9", spacing3=4)

# Greeting
chat_box.config(state=tk.NORMAL)
chat_box.insert(tk.END, "  🎓 Bot  \n", "bot_tag")
chat_box.insert(tk.END, "  Hello! Welcome to the College Helpdesk.\n  How can I help you today?\n\n", "bot_msg")
chat_box.config(state=tk.DISABLED)

# --- Input Area ---
input_frame = tk.Frame(root, bg="#f5f7ff", pady=10)
input_frame.pack(fill=tk.X, padx=12)

entry = tk.Entry(input_frame, font=("Helvetica", 12),
                 bg="#ffffff", fg="#222222", relief=tk.GROOVE, bd=2)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
entry.bind("<Return>", send_message)
entry.focus()

send_btn = tk.Button(input_frame, text="Send ➤",
                     font=("Helvetica", 11, "bold"),
                     bg="#4a90d9", fg="white",
                     relief=tk.FLAT, padx=16, pady=10,
                     cursor="hand2", command=send_message,
                     activebackground="#357abd", activeforeground="white")
send_btn.pack(side=tk.RIGHT)

# --- Footer ---
tk.Label(root, text="Powered by NLTK + WordNet",
         font=("Helvetica", 8), bg="#f5f7ff", fg="#aaaaaa").pack(pady=(0, 8))

root.mainloop()