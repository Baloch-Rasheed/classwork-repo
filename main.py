# from vigenere_cipher import vigenere_cipher
from mini_des import mini_des_algorithm as mini


def main():

    mini_des = mini.Mini_DES()
    mini_des.sub_gen()
    # key = 0b10110101
    # message = 'my message is encrypted'
    # mini = mn.MiniDES(data=message, key=key, block_size=8, round = 2)
    # print('Key is :', bin(key))
    
    # result = mini.encrypt()
    # print('plain Message: ' + message + f'| length: {len(message)}')
    # print('Encryped Message: ' + result + f'| length: {len(result)}')

    
    # print('Decryped Message: '+ mini.decrypt(result))
    print('Mini-DES')

            
    


# def main():
#     print('hello world')

#     message = 'Try to write your message here'
#     keyword = 'Secret'

#     print('Plain Text: ', message)
#     encrypted_message = vigenere_cipher.encrypt(message=message, key_phrase=keyword)
#     print('Encrypted Text: ', encrypted_message)

#     decrypted_message = vigenere_cipher.decrypt(encrypted=encrypted_message, key_phrase=keyword)
#     print('Decrypted Text: ', decrypted_message)


if __name__ == "__main__":
    main()