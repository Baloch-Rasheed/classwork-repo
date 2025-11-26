from Crypto.Hash import MD5, SHA1, SHA256
from Crypto.Util.Padding import pad
from base64 import b64encode 

class HashAl:

    def message_hash(self, data):
        padded_data = pad(data.encode(), MD5.block_size)
        cipher = MD5.new(padded_data)
        return b64encode(cipher.digest())
    
    def text_doc_hash(self, path_to_file):

        cipher = MD5.new()

        with open(path_to_file, 'rb') as file:
            while True:
                piece = file.read(512)
                if not piece:
                    break
                cipher.update(piece)
        return b64encode(cipher.digest())
