from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

class AES_Alg:

    def encrypt(self, key, message):
        iv = get_random_bytes(16)
        padded_message = pad(message.encode(), AES.block_size)
        aes_cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        cipher_bytes = aes_cipher.encrypt(padded_message)
        return b64encode(iv + cipher_bytes)
    
    def decrypt(self, key, cipher_text):
        cipher_text = b64decode(cipher_text)
        iv = cipher_text[:16]
        cipher_text = cipher_text[16:]
        aes_cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        decoded_cipher_text = cipher_text
        plain_bytes = aes_cipher.decrypt(decoded_cipher_text)
        plain_text = unpad(plain_bytes, AES.block_size)
        return plain_text.decode()