'''
import qrcode
from cryptography.fernet import Fernet  # Example encryption library

# Encrypt your data
key = Fernet.generate_key()
cipher_suite = Fernet(key)
data_to_encrypt = "Your secret data"
encrypted_data = cipher_suite.encrypt(data_to_encrypt.encode('utf-8'))

# Generate a QR code with the encrypted data
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encrypted_data)
qr.make(fit=True)

# Create a QR code image
qr_code = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image to a file
qr_code.save("encrypted_qr.png")
'''
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

def derive_key(password):
    salt = b'some_salt_value'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for AES-256
        salt=salt,
        iterations=100000,  # adjust based on your security requirements
        backend=default_backend()
    )
    return kdf.derive(password)

def encrypt_text(plaintext, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(ciphertext).decode('utf-8')

def decrypt_text(ciphertext, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(b64decode(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode('utf-8')

# Example usage:
password = b'some_secret_password'
key = derive_key(password)
plaintext = 'Hello, this is a secret message!'
encrypted_data = encrypt_text(plaintext, key)
print(f'Encrypted Data: {encrypted_data}')

decrypted_data = decrypt_text(encrypted_data, key)
print(f'Decrypted Data: {decrypted_data}')