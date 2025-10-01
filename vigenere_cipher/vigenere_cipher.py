def encrypt(message, key_phrase):
    result = ''
    i = 0
    for char in message:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                key_char = key_phrase[i % len(key_phrase)]
                key_position = ord(key_char) - base
                char_position = ord(char) - base
                new_position = (char_position + key_position) % 26
                result += chr(new_position + base)
            else:
                base = ord('a')
                key_char = key_phrase[i % len(key_phrase)]
                key_position = ord(key_char) - base
                char_position = ord(char) - base
                new_position = (char_position + key_position) % 26
                result += chr(new_position + base)
            i += 1
        else:
            result += char
    return result

def decrypt(encrypted, key_phrase):
    result = ''
    i = 0
    for char in encrypted:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                new_key_index = i % len(key_phrase)
                key_char = key_phrase[new_key_index]
                key_position = ord(key_char) - base
                char_position = ord(char) - base
                new_position = (char_position - key_position + 26) % 26
                result += chr(new_position + base)
            else:
                base = ord('a')
                new_key_index = i % len(key_phrase)
                key_char = key_phrase[new_key_index]
                key_position = ord(key_char) - base
                char_position = ord(char) - base
                new_position = (char_position - key_position + 26) % 26
                result += chr(new_position + base)
            i += 1
        else:
            result += char
    return result



                