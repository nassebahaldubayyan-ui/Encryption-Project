import tkinter as tk
from tkinter import messagebox
import base64
from crypto_utils import encrypt_text, decrypt_text


# =========================
# Encrypt + Decrypt Function
# =========================
def process_text():

    plaintext = message_input.get("1.0", tk.END).strip()
    password = password_input.get().strip()

    # Validation
    if not plaintext or not password:
        messagebox.showerror(
            "Error",
            "Please enter both message and password."
        )
        return

    try:
        # Encrypt
        encrypted_data = encrypt_text(password, plaintext)

        # Decrypt
        decrypted_text = decrypt_text(password, encrypted_data)

        # Show encrypted text
        encrypted_output.config(state="normal")
        encrypted_output.delete("1.0", tk.END)

        encrypted_output.insert(
            tk.END,
            encrypted_data["ciphertext"].hex()
        )

        encrypted_output.config(state="disabled")

        # Show decrypted text
        decrypted_output.config(state="normal")
        decrypted_output.delete("1.0", tk.END)

        decrypted_output.insert(
            tk.END,
            decrypted_text
        )

        decrypted_output.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# =========================
# Main Window
# =========================
root = tk.Tk()
root.title("AES Encryption System")
root.geometry("700x600")


# =========================
# Message Input
# =========================
message_label = tk.Label(root, text="Enter Message:")
message_label.pack(pady=5)

message_input = tk.Text(root, height=6, width=70)
message_input.pack(pady=5)


# =========================
# Password Input
# =========================
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_input = tk.Entry(root, width=50, show="*")
password_input.pack(pady=5)


# =========================
# Encrypt Button
# =========================
encrypt_button = tk.Button(
    root,
    text="Encrypt",
    command=process_text
)
encrypt_button.pack(pady=15)


# =========================
# Encrypted Output
# =========================
encrypted_label = tk.Label(root, text="Encrypted Text:")
encrypted_label.pack()

encrypted_output = tk.Text(root, height=6, width=80)
encrypted_output.pack(pady=5)
encrypted_output.config(state="disabled")


# =========================
# Decrypted Output
# =========================
decrypted_label = tk.Label(root, text="Decrypted Text:")
decrypted_label.pack()

decrypted_output = tk.Text(root, height=6, width=80)
decrypted_output.pack(pady=5)
decrypted_output.config(state="disabled")


# Run App
root.mainloop()