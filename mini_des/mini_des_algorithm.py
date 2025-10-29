class Mini_DES:

    def __init__(self, key, data, round = 2):
        self._key = key
        self._plain_text = data
        self._round = round
    

        
    def sub_key_gen(self):
        self.key
        self._modified_key = bin((self.key << 1 | self.key >> 7) & 0xFF)
        self._subkeys = []
        self._subkeys.append( self._modified_key & 0xF )
        self._subkeys.append( (self._modified_key >> 4) & 0xF )

    def f(self, right_half, sub_key):
        return right_half ^ sub_key
    
    def encrypt(self):

        cipher_text = ""
        for spell in self._plain_text:
            right_half = bin(ord(spell)) & 0xF
            left_half = (bin(ord(spell)) >> 4) & 0xF
            for i  in range(self._round):
                temp = left_half
                left_half = right_half
                right_half = temp ^ self.f(right_half, self._subkeys[i])
            cipher_text += bin(left_half) + bin(right_half)[2:]


        
        