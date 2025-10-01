def encrypt_message(message, key):
    result = ''
    for item in message:
        if item.isalpha():
            if item.isupper():
                base = ord('A')
                calculated_base = ord(item) - base
                new_position = (calculated_base + key) % 26
                result += chr(new_position + base)
            else:
                base = ord('a')
                calculated_base = ord(item) - base
                new_position = (calculated_base + key) % 26
                result += chr(new_position + base)
        else:
            result += item
    return result

def decrypt_message(encrypted_message, key):
    result = encrypt_message(encrypted_message, (-1 * key))
    return result

