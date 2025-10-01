from vigenere_cipher import vigenere_cipher


def main():
    print('hello world')

    message = 'Try to write your message here'
    keyword = 'Secret'

    print('Plain Text: ', message)
    encrypted_message = vigenere_cipher.encrypt(message=message, key_phrase=keyword)
    print('Encrypted Text: ', encrypted_message)

    decrypted_message = vigenere_cipher.decrypt(encrypted=encrypted_message, key_phrase=keyword)
    print('Decrypted Text: ', decrypted_message)


if __name__ == "__main__":
    main()