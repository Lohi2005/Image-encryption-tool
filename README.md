# 🔐 Image Encryption Tool – XOR-Based Pixel Manipulation

This project was developed as part of the Skill Craft Cybersecurity Internship (Task 2). It demonstrates a simple image encryption and decryption tool using pixel-level XOR operations in Python.

## 📌 Objective
Encrypt and decrypt images using lightweight, reversible pixel manipulation techniques. The tool uses XOR logic to transform image data securely and efficiently.

## 🛠 Features
- XOR-based encryption and decryption
- Random key generation and secure key reuse
- Key saved as JSON for reproducible decryption
- Compatible with most image formats (PNG, JPG, etc.)
- Optional inline display for Jupyter environments

## 🧠 Key Learnings
- Image data manipulation using NumPy arrays
- Basic cryptographic logic with XOR operations
- Key management for secure and reversible encryption
- Integration with Pillow for image processing

## 🚀 Technologies Used
- Python
- Pillow (PIL)
- NumPy
- JSON

## 📷 How It Works
1. Load image and convert to NumPy array
2. Generate a random key matching the image shape
3. Apply XOR operation between image pixels and key
4. Save encrypted image and key
5. Decrypt using the same key

## 📂 File Structure
├── encryption_key.json # Stores the generated key ├── encrypted_image.png # Output of encryption ├── decrypted_image.png # Output of decryption ├── image_encryptor.py # Main script └── README.md

Code

## ▶️ Usage

### 1. Run the Script
```bash
python image_encryptor.py
2. Choose Mode
E for encryption

D for decryption

3. Provide Image Path
For encryption, input the path to your image file.

For decryption, ensure encryption_key.json and encrypted_image.png exist.

Example
bash
Choose mode (E for encrypt, D for decrypt): e
Enter the path to the image file: 
