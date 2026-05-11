import tkinter as tk
from tkinter import messagebox
from crypto_utils import encrypt_text, decrypt_text


# Encrypt + Decrypt Function
def process_text():

    plaintext = message_input.get("1.0", tk.END).strip()
    password = password_input.get().strip()

    # Validation
    if not plaintext or not password:
        messagebox.showerror("Error","Please enter both message and password.")
        return

    try:
        # Encrypt
        encrypted_data = encrypt_text(password, plaintext)

        # Decrypt
        decrypted_text = decrypt_text(password, encrypted_data)

        # Show encrypted text
        encrypted_output.config(state="normal")
        encrypted_output.delete("1.0", tk.END)
        encrypted_output.insert(tk.END, encrypted_data["ciphertext"].hex())
        encrypted_output.config(state="disabled")

        # Show decrypted text
        decrypted_output.config(state="normal")
        decrypted_output.delete("1.0", tk.END)
        decrypted_output.insert(tk.END, decrypted_text)
        decrypted_output.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main Window
root = tk.Tk()
root.title("AES Encryption System")
root.geometry("500x380") 

# Message section 
message_label = tk.Label(root, text="Enter Message:")
message_label.pack(pady=5)
#to input message
message_input = tk.Text(root, height=2, width=50)
message_input.pack(pady=5)

# Password section
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)
#to input password
password_input = tk.Entry(root, width=50, show="*")
password_input.pack(pady=5)

# Encrypt Button
encrypt_button = tk.Button(root,text="Encrypt",command=process_text,bg="lightblue",fg="black",activebackground="darkblue",activeforeground="white", width=15)
encrypt_button.pack(pady=15)

# Encrypted Output section
encrypted_label = tk.Label(root, text="Encrypted Text:")
encrypted_label.pack()
#to show encrypted text
encrypted_output = tk.Text(root, height=2, width=50)
encrypted_output.pack(pady=5)
encrypted_output.config(state="disabled")

# Decrypted Output section
decrypted_label = tk.Label(root, text="Decrypted Text:")
decrypted_label.pack()
#to show decrypted text
decrypted_output = tk.Text(root, height=2, width=50)
decrypted_output.pack(pady=5)
decrypted_output.config(state="disabled")

# Run App
root.mainloop()