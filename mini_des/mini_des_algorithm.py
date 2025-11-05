class Mini_DES:

    def __init__(self, key, data, round = 2):
        self._key = key
        self._plain_text = data
        self._round = round
    

        
    def sub_key_gen(self):
        self._modified_key = (self._key << 1 | self._key >> 7) & 0xFF
        self._subkeys = []
        self._subkeys.append( self._modified_key & 0xF )
        self._subkeys.append( (self._modified_key >> 4) & 0xF )

    def f(self, right_half, sub_key):
        return right_half ^ sub_key
    
    def encrypt(self):

        cipher_text = ""
        for spell in self._plain_text:
            right_half = ord(spell) & 0xF
            left_half = (ord(spell) >> 4) & 0xF
            for i  in range(self._round):
                temp = left_half
                left_half = right_half
                right_half = temp ^ self.f(right_half, self._subkeys[i])
            cipher_text_char = (left_half << 4) | right_half
            cipher_text += chr(cipher_text_char)
        return cipher_text
    
    def decrypt(self, cipher_text):
        plain_text = ""
        for spell in cipher_text:
            right_half = ord(spell) & 0xF
            left_half = (ord(spell) >> 4) & 0xF
            for i  in range(self._round - 1, -1,-1):
                temp = right_half
                right_half = left_half
                left_half = temp ^ self.f(left_half, self._subkeys[i])
            cipher_text_char = (left_half << 4) | right_half
            plain_text += chr(cipher_text_char)
        return plain_text

        
        