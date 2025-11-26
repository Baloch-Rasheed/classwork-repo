# from vigenere_cipher import vigenere_cipher
# from mini_des import mini_des_algorithm as md
# from aes_algorithms import AES_Alg
from hash_algorithm import HashAl



def main():

    key = 'abcdabcdabcdabcd'
    message = "This is information security class"
    message2 = "This is information security class "

    print('Plain Text:'+ message)

    hs = HashAl()
    results = hs.message_hash(message)
    results2 = hs.message_hash(message2)
    results3 = hs.text_doc_hash('documents.txt')

    print(f"Hash Key: {results}")
    print(f"Hash Key 2: {results2}")
    print(f"File Hash Key: {results3}")



    # aes = AES_Alg()

    # encrypted_text = aes.encrypt(key, message)
    # encrypted_text2 = aes.encrypt(key, message)

    # print('Plain Text:'+ message)
    # print(f'Encrypted Text: '+ encrypted_text.decode())
    # print(f'Encrypted Text 2: '+ encrypted_text2.decode())

    # decrypted_text = aes.decrypt(key, encrypted_text2)
    # print(f'Decrypted Text 2: '+ decrypted_text)


    # mini_des = md.Mini_DES(key=key, data=message)

    # mini_des.sub_key_gen()
    # cipher_text = mini_des.encrypt()
    # print('Plain_Text :'+ message)
    # print('Encrypted Text: ' + cipher_text)

    # plain_text = mini_des.decrypt(cipher_text)
    # print('Decrypted Text: '+ plain_text)
    
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