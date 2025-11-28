from Crypto.Hash import MD5, SHA1, SHA256
from Crypto.Util.Padding import pad
from base64 import b64encode

class HashAl:

    def message_hash(self, message):
        padded_message = pad(message.encode(), MD5.block_size)
        cipher = MD5.new(padded_message)
        return b64encode(cipher.digest()).decode()

