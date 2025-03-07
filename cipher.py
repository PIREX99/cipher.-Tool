import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter.font as tkFont

# Function to perform Caesar Cipher Encryption
def encrypt_text():
    text = text_area.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    
    if not text or not shift.isdigit():
        messagebox.showerror("Error", "Please enter valid text and shift value.")
        return
    
    shift = int(shift)
    encrypted_text = "".join(
        chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
        for char in text
    )
    result_label.config(text=f"Encrypted: {encrypted_text}", fg="#00FF00")

# Function to perform Caesar Cipher Decryption
def decrypt_text():
    text = text_area.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    
    if not text or not shift.isdigit():
        messagebox.showerror("Error", "Please enter valid text and shift value.")
        return
    
    shift = int(shift)
    decrypted_text = "".join(
        chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else
        chr(((ord(char) - 97 - shift) % 26) + 97) if char.islower() else char
        for char in text
    )
    result_label.config(text=f"Decrypted: {decrypted_text}", fg="#FF0000")

# Function to copy the result text
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Info", "Text copied to clipboard!")

# Function to paste text into the text area
def paste_text():
    try:
        clipboard_text = root.clipboard_get()
        text_area.insert(tk.END, clipboard_text)
    except tk.TclError:
        messagebox.showerror("Error", "No text found in clipboard!")

# Creating the main application window
root = tk.Tk()
root.title("Caesar Cipher - CyberSec Edition")
root.geometry("600x500")
root.configure(bg="#0A0A0A")
root.resizable(False, False)

# Custom Font
font_style = tkFont.Font(family="Courier", size=12, weight="bold")

# Header Frame
header_frame = tk.Frame(root, bg="#0A0A0A", pady=10)
header_frame.pack(fill="x", padx=20)
title_label = tk.Label(header_frame, text=" Cipher CyberSec Edition", font=("Courier", 16, "bold"), fg="#00FF00", bg="#0A0A0A")
title_label.pack()

# Main Body Frame
body_frame = tk.Frame(root, bg="#0A0A0A", padx=20)
body_frame.pack(pady=20, fill="both", expand=True)

# Text Area
text_area = scrolledtext.ScrolledText(body_frame, height=5, width=55, font=font_style, bg="#1E1E1E", fg="#00FF00", insertbackground="white", borderwidth=3, relief="ridge")
text_area.pack(pady=10)

# Shift Value Label
shift_label = tk.Label(body_frame, text="Shift Value:", font=font_style, fg="#FFFFFF", bg="#0A0A0A")
shift_label.pack()

# Shift Entry
shift_entry = tk.Entry(body_frame, font=font_style, width=5, bg="#1E1E1E", fg="#00FF00", insertbackground="white", borderwidth=3, relief="ridge")
shift_entry.pack(pady=5)

# Encrypt and Decrypt Buttons
encrypt_button = tk.Button(body_frame, text="Encrypt", font=font_style, bg="#008000", fg="#FFFFFF", command=encrypt_text, borderwidth=3, relief="ridge")
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(body_frame, text="Decrypt", font=font_style, bg="#800000", fg="#FFFFFF", command=decrypt_text, borderwidth=3, relief="ridge")
decrypt_button.pack(pady=5)

# Result Label
result_label = tk.Label(body_frame, text="", font=font_style, fg="#FFFFFF", bg="#0A0A0A")
result_label.pack(pady=10)

# Copy and Paste Buttons
copy_button = tk.Button(body_frame, text="Copy Result", font=font_style, bg="#0000FF", fg="#FFFFFF", command=copy_text, borderwidth=3, relief="ridge")
copy_button.pack(pady=5)

paste_button = tk.Button(body_frame, text="Paste Text", font=font_style, bg="#FF6600", fg="#FFFFFF", command=paste_text, borderwidth=3, relief="ridge")
paste_button.pack(pady=5)

# Footer Frame
footer_frame = tk.Frame(root, bg="#0A0A0A", pady=10)
footer_frame.pack(fill="x", padx=20, side="bottom")
developer_label = tk.Label(footer_frame, text="Developed by PIREX", font=("Courier", 10, "italic"), fg="#00FFFF", bg="#0A0A0A")
developer_label.pack()

# Run the GUI application
root.mainloop()
