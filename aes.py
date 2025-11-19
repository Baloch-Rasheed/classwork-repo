from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

class AES_Algorithm:

    def encrypt(self, key, message):
        iv = get_random_bytes(16)
        message_byte = pad(message.encode(), AES.block_size)
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        cipher_text = cipher.encrypt(message_byte)
        return b64encode(iv + cipher_text)
    
    def decrypt(self, key, cipher_text):
        new_cipher_text = b64decode(cipher_text.decode())
        iv = new_cipher_text[:16]
        new_cipher_text = new_cipher_text[16:]
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        plain_bytes = cipher.decrypt(new_cipher_text)
        unpadded_message = unpad(plain_bytes, AES.block_size)
        return unpadded_message.decode()