from key_encryptor import crypt_key

#key is an array of numbers where each number represents an offsent
#key can also be a string of letters - each letter assigned to its order in the alphabet
#becomes the key used to encrypt by vigenere encryption
def encrypt(message, key):
    
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for element in message.lower():

        # Append any non-letter character to the message
        if not element.isalpha():
            final_message += element
            
        else:        
            # Find the right key character to offset
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(element)

            #if the key is string
            if type (element) is str:
                offset = alphabet.index(key_char)
            
            #if the key is an array of numbers
            if type (element) is int:
                offset = element
              
            new_index = (index + offset) % len(alphabet)
            final_message += alphabet[new_index]
    
    print (final_message)
    print (crypt_key(key))

#encrypt("Hello!! World", "dfpokjksfghdhfmcgjemskd")
