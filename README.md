# AES Encryption System (Python Project)

## Project Overview
This project is a simple but secure encryption and decryption system built using Python.  
It allows users to enter a message and a password, then encrypts the message and immediately decrypts it to verify correctness.

The system demonstrates how modern cryptography works using secure algorithms like AES-GCM and PBKDF2.

---

## Team members

- **Rahaf Obaid Alharbi 432218745**
- **Badriah Alharbi 431201871**
- **Nasseebah Rashed Aldubayyan 431201800**

---

## Features

- Encrypts user messages securely
- Decrypts encrypted messages back to original text
- Password-based encryption system
- Graphical User Interface (GUI) using Tkinter
- Verification system to ensure encryption correctness
- Clean and simple user experience

---

## Technologies Used

- Python
- Tkinter (GUI)
- PyCryptodome library
- AES-GCM encryption :contentReference[oaicite:0]{index=0}
- PBKDF2 key derivation :contentReference[oaicite:1]{index=1}

---

## How the System Works

### 1. Key Generation
A secure encryption key is generated from the user password using PBKDF2.

### 2. Encryption
The message is encrypted using AES-GCM which ensures:
- Confidentiality (no one can read the message)
- Integrity (data cannot be modified)

### 3. Decryption
The encrypted message is decrypted back to its original form using the same password.

### 4. Verification
The system automatically compares decrypted text with original input to ensure correctness.

---

## Project Structure
Encryption-Project/
│
├── crypto_utils.py # Encryption & decryption logic
├── verifier.py # GUI application (main system)
└── README.md # Project documentation

---

## How to Run the Project

### 1. Install required library
pip install pycryptodome

### 2. run verifier.py
python EncryptionProject/verifier.py

---

### How to Use
1. Open the program
2. Enter a message in the text box
3. Enter a password
4. Click Encrypt
5. View:
    A. Encrypted text
    b. Decrypted text (verification result)
