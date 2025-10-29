class Mini_DES:

    def __init__(self, key, data):
        self._plain_text = data
        self._key = key

    def sub_gen(self):
        self._modified_key = (self._key << 1 | self._key >> 7) & 0xFF
        self._sub_keys = []
        self._sub_keys.append(self._modified_key & 0xF)
        self._sub_keys.append((self._modified_key >> 4) & 0xF)

    def f(right_half, sub_key):
        return right_half ^ sub_key

    def round(self, left_half, right_half, sub_key):
        left_half = right_half
        right_half = left_half ^ self.f(right_half, sub_key)
        return left_half, right_half

    def encrypt(self):
        cipher_text = ''
        for block in self._plain_text:
            binary_block = int(ord(block), 2)
            