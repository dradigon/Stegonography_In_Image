# Image Encryption & Decryption using GUI

## 📌 Project Overview
This project provides a **user-friendly GUI application** that allows users to **securely encrypt and decrypt messages inside images** using **password protection**. The encryption process modifies pixel values to store the hidden message, ensuring data confidentiality.

## 🛠️ Technologies Used
- **Python** (Programming Language)
- **Tkinter** (GUI Development)
- **OpenCV (cv2)** (Image Processing)
- **Pillow** (Image Handling)

## 📷 Features
✅ **User-Friendly Interface** – Simple GUI for easy usage  
✅ **Secure Message Hiding** – Uses pixel-based encryption  
✅ **Password Protection** – Ensures only authorized decryption  
✅ **Supports Multiple Image Formats** – Works with PNG and JPG  

## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, run:
```sh
pip install opencv-python pillow
```

### 2️⃣ Run the Encryption GUI
```sh
python e.py
```
- Select an image.
- Enter a **message and password**.
- Click **Encrypt** to generate `encryptedImage.png`.

### 3️⃣ Run the Decryption GUI
```sh
python d.py
```
- Select the **encrypted image**.
- Enter the **correct password**.
- Click **Decrypt** to retrieve the hidden message.



## 📎 Repository Structure
```
📂 Project Folder
│-- e.py  # Encryption GUI
│-- d.py  # Decryption GUI
│-- README.md  # Project Documentation
│-- myimage.png  # Output Image
```

## 🔗 Future Enhancements
🚀 **Planned Features:**
- Implement **AES Encryption** for enhanced security  
- Add **Drag & Drop Support** for file selection  
- Convert into a **Mobile Application**  

## 💡 Contribution
Feel free to fork this repo, make improvements, and submit pull requests! 😊


## 📬 Contact
For any queries, reach out at https://github.com/dradigon
