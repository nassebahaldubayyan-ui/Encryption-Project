import tkinter as tk
from tkinter import messagebox
import base64

from crypto_utils import encrypt_text, decrypt_text


# =========================
# Encrypt + Decrypt
# =========================
def process_text():

    plaintext = message_input.get("1.0", tk.END).strip()
    password = password_input.get().strip()

    if not plaintext or not password:
        messagebox.showerror("Error", "Enter both message and password")
        return

    try:
        encrypted_data = encrypt_text(password, plaintext)
        decrypted_text = decrypt_text(password, encrypted_data)

        # Convert to Base64 (clean display)
        encoded_cipher = base64.b64encode(
            encrypted_data["ciphertext"]
        ).decode()

        # Show encrypted
        encrypted_output.config(state="normal")
        encrypted_output.delete("1.0", tk.END)
        encrypted_output.insert(tk.END, encoded_cipher)
        encrypted_output.config(state="disabled")

        # Show decrypted
        decrypted_output.config(state="normal")
        decrypted_output.delete("1.0", tk.END)
        decrypted_output.insert(tk.END, decrypted_text)
        decrypted_output.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# Copy Function
# =========================
def copy_encrypted():
    text = encrypted_output.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Encrypted text copied!")


# =========================
# UI
# =========================
root = tk.Tk()
root.title("AES Encryption System")
root.geometry("700x650")


# Message
tk.Label(root, text="Enter Message:").pack(pady=5)
message_input = tk.Text(root, height=6, width=70)
message_input.pack(pady=5)

# Password
tk.Label(root, text="Enter Password:").pack(pady=5)
password_input = tk.Entry(root, width=50, show="*")
password_input.pack(pady=5)


# Encrypt Button
tk.Button(root, text="Encrypt", command=process_text).pack(pady=10)


# Encrypted Output
tk.Label(root, text="Encrypted Text (Base64):").pack()

encrypted_output = tk.Text(root, height=5, width=80)
encrypted_output.pack(pady=5)
encrypted_output.config(state="disabled")

tk.Button(root, text="Copy Encrypted Text", command=copy_encrypted).pack(pady=5)


# Decrypted Output
tk.Label(root, text="Decrypted Text:").pack()

decrypted_output = tk.Text(root, height=5, width=80)
decrypted_output.pack(pady=5)
decrypted_output.config(state="disabled")


root.mainloop()