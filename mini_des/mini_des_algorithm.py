class Mini_DES:

    def __init__(self, key, data, rounds):
        self._plain_text = data
        self._key = key
        self._rounds = rounds

    def sub_key_gen(self):
        self._modified_key = (self._key << 1 | self._key >> 7) & 0xFF
        self._sub_keys = []
        self._sub_keys.append(self._modified_key & 0xF)
        self._sub_keys.append((self._modified_key >> 4) & 0xF)

    def f(self,right_half, sub_key):
        return right_half ^ sub_key

    def encrypt(self):
        cipher_text = ''
        for block in self._plain_text:
            binary_block = ord(block)
            "1001   0101"
            right_half = binary_block & 0xF
            left_half = (binary_block >> 4) & 0xF
            for i in range(self._rounds):
                temp = left_half
                left_half = right_half
                right_half = temp ^ self.f(right_half, self._sub_keys[i])
            binary_cipher_block = (left_half << 4) | right_half
            cipher_text += chr(binary_cipher_block)
        return cipher_text

    def decrypt(self, cipher_text):
        plain_text = ''
        for blocks in cipher_text:
            binary_block = ord(blocks)
            right_half = binary_block & 0xF
            left_half = (binary_block >> 4) & 0xF
            for i in range(self._rounds -1 , -1, -1):
                temp  = right_half
                right_half = left_half
                left_half = temp ^ self.f(left_half, self._sub_keys[i])
            
            binary_plain_text_block = (left_half << 4) | right_half
            plain_text += chr(binary_plain_text_block)
        return plain_text
            