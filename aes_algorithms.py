from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode

class AES_Alg:

    def encrypt(self, key, message):
        padded_message = pad(message.encode(), AES.block_size)
        aes_cipher = AES.new(key.encode(), AES.MODE_ECB)
        cipher_bytes = aes_cipher.encrypt(padded_message)
        return b64encode(cipher_bytes)
    
    def decrypt(self, key, cipher_text):
        aes_cipher = AES.new(key.encode(), AES.MODE_ECB)
        decoded_cipher_text = b64decode(cipher_text)
        plain_bytes = aes_cipher.decrypt(decoded_cipher_text)
        plain_text = unpad(plain_bytes, AES.block_size)
        return plain_text.decode()