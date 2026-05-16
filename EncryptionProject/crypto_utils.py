from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


# =========================
# Key Derivation Function
# =========================
def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=100000)


# =========================
# Encrypt Text
# =========================
def encrypt_text(password, plaintext):
    # Convert text to bytes
    data = plaintext.encode()

    # Generate random salt
    salt = get_random_bytes(16)

    # Derive encryption key
    key = derive_key(password, salt)

    # Create AES-GCM cipher
    cipher = AES.new(key, AES.MODE_GCM)

    # Encrypt data
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return {
        "salt": salt,
        "key": key,
        "nonce": cipher.nonce,
        "tag": tag,
        "ciphertext": ciphertext
    }


# =========================
# Decrypt Text
# =========================
def decrypt_text(password, enc_data):
    # Recreate key from password and salt
    key = derive_key(password, enc_data["salt"])

    # Create AES-GCM cipher with nonce
    cipher = AES.new(
        key,
        AES.MODE_GCM,
        nonce=enc_data["nonce"]
    )

    # Decrypt and verify integrity
    data = cipher.decrypt_and_verify(
        enc_data["ciphertext"],
        enc_data["tag"]
    )

    # Convert bytes back to string
    return data.decode()

