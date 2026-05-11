from crypto_utils import encrypt_text, decrypt_text

print("AES Text Encryption Tool")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose (1/2): ")
password = input("Enter password: ")

if choice == "1":
    text = input("Enter text to encrypt: ")
    encrypted = encrypt_text(password, text)

    print("\nEncrypted Data:")
    print(encrypted)

elif choice == "2":
    print("Paste encrypted data (as dictionary):")
    enc_input = input()

    enc_data = eval(enc_input)

    decrypted = decrypt_text(password, enc_data)

    print("\nDecrypted Text:")
    print(decrypted)

else:
    print("Invalid choice")
