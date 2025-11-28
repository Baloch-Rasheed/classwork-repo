# from vigenere_cipher import vigenere_cipher
from mini_des import mini_des_algorithm as md
from aes import AES_Algorithm
from hash_algorithm import HashAl



def main():

    key = 'abcdefghijklmnop'
    message = "This is information security class"
    message2 = "This is information security class "
    print(f"Plain Text: {message}")

    hs = HashAl()

    digest =  hs.message_hash(message)
    digest2 =  hs.message_hash(message2)
    print(f'Digest :{digest}')
    print(f'Digest 2 :{digest2}')

    
    # aes = AES_Algorithm()

    # encrypted_text = aes.encrypt(key, message)

    # print(f"Plain Text: {message}")
    # print(f"Encrypted Text: "+ encrypted_text.decode())

    # encrypted_text2 = aes.encrypt(key, message)

    # print(f"Encrypted Text 2: "+ encrypted_text2.decode())

    # decrypted_text = aes.decrypt(key, encrypted_text)
    # print("Decrypted Text: "+ decrypted_text)
    
    # mini_des = md.Mini_DES(key=key, data=message, rounds=2)

    # mini_des.sub_key_gen()
    # cipher_text = mini_des.encrypt()
    # print('Plain_Text :'+ message)
    # print('Encrypted Text: ' + cipher_text)

    # decrypted_text = mini_des.decrypt(cipher_text)

    # print('Decrypted Text: '+ decrypted_text)

    # text = mini_des.decrypt(cipher_text)
    # print('Decrypted Text: '+ text)
    
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