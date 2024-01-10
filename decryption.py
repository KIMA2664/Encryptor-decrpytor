from key_encryptor import crypt_key

#key is an array of numbers obtained by RSA encryption
#becomes the key used to encrypt by vigenere encryption
def decrypt(message, key):
    
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    decrypt_key = crypt_key (key, -1)

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
            
        else:        
            # Find the right key character to offset
            offset = decrypt_key[key_index % len(key)]
            key_index += 1

            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)
            final_message += alphabet[new_index]
    
    print (final_message)


#decrypt ("kjazy!! fyjqj" ,[33, 17, 29, 2, 32, 25, 32, 18, 17, 4, 7, 33, 7, 17, 12, 22, 4, 25, 28, 12, 18, 32, 33])