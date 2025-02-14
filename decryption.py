import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_label.config(text=f"Selected: {os.path.basename(file_path)}")
        app.selected_file = file_path

def decrypt_message():
    if not hasattr(app, 'selected_file') or not app.selected_file:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    password = pass_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return
    
    img = cv2.imread(app.selected_file)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    message_bytes = []
    m, n, z = 0, 0, 0
    while True:
        char = img[n, m, z]
        if char == 126:  # '~' indicates end of message
            break
        message_bytes.append(char)
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    decrypted_text = bytes(message_bytes).decode('utf-8')
    stored_password, message = decrypted_text.split('|', 1)
    
    if password == stored_password:
        messagebox.showinfo("Decryption Success", f"Decrypted Message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect password!")

# GUI Setup
app = tk.Tk()
app.title("Image Decryption")
app.geometry("500x400")
app.configure(bg="#34495e")

title_label = tk.Label(app, text="🔓 Image Decryptor", font=("Arial", 14, "bold"), bg="#34495e", fg="white")
title_label.pack(pady=10)

image_label = tk.Label(app, text="No file selected", bg="#34495e", fg="white")
image_label.pack()

select_button = tk.Button(app, text="Choose Image", command=select_image, bg="#e74c3c", fg="white", font=("Arial", 12))
select_button.pack(pady=5)

pass_entry = tk.Entry(app, width=40, show="*")
pass_entry.pack(pady=5)
pass_entry.insert(0, "Enter password")

decrypt_button = tk.Button(app, text="Decrypt Message", command=decrypt_message, bg="#2ecc71", fg="white", font=("Arial", 12))
decrypt_button.pack(pady=5)

app.mainloop()
