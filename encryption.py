import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_label.config(text=f"Selected: {os.path.basename(file_path)}")
        app.selected_file = file_path


def encrypt_message():
    if not hasattr(app, 'selected_file') or not app.selected_file:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    message = msg_entry.get()
    password = pass_entry.get()
    
    if not message or not password:
        messagebox.showerror("Error", "Please enter both a message and a password!")
        return
    
    img = cv2.imread(app.selected_file)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    full_message = password + "|" + message + "~"
    message_bytes = full_message.encode('utf-8')
    m, n, z = 0, 0, 0
    
    for byte in message_bytes:
        img[n, m, z] = byte
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    output_path = "encryptedImage.png"
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", "Message encrypted and saved as encryptedImage.png!")


# GUI Setup
app = tk.Tk()
app.title("Image Encryption")
app.geometry("500x400")
app.configure(bg="#2c3e50")

title_label = tk.Label(app, text="🔒 Image Encryptor", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

image_label = tk.Label(app, text="No file selected", bg="#2c3e50", fg="white")
image_label.pack()

select_button = tk.Button(app, text="Choose Image", command=select_image, bg="#3498db", fg="white", font=("Arial", 12))
select_button.pack(pady=5)

msg_entry = tk.Entry(app, width=40)
msg_entry.pack(pady=5)
msg_entry.insert(0, "Enter secret message")

pass_entry = tk.Entry(app, width=40, show="*")
pass_entry.pack(pady=5)
pass_entry.insert(0, "Enter password")

encrypt_button = tk.Button(app, text="Encrypt Message", command=encrypt_message, bg="#27ae60", fg="white", font=("Arial", 12))
encrypt_button.pack(pady=5)

app.mainloop()
