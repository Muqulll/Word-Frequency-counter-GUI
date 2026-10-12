import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

root = ctk.CTk()
root.title("Word Frequency Counter")
root.geometry("420x300")
ctk.set_appearance_mode("light")
style = ttk.Style()
style.theme_use("clam")  # Allows more style customization on many systems
style.configure("TFrame", background="#20242b")
style.configure("TLabel", background="#20242b", foreground="#f1f3f5")
style.configure("TButton", padding=8)
style.configure("TEntry", padding=6)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Word Frequency Counter",
          font=("Arial", 16, "bold")).pack(pady=(0, 12))

entry = ctk.CTkEntry(frame,corner_radius=12, placeholder_text="Type words separated by spaces")
entry.pack(fill="x", pady=6)

result = ttk.Label(frame, text="Results will appear here")
result.pack(pady=12)

def count_words():
    words = entry.get().lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    result.config(text=str({w: n for w, n in counts.items() if n > 1}))

ctk.CTkButton(frame, text="Count repeated words", corner_radius=12,command=count_words).pack(pady=6)

root.mainloop()
