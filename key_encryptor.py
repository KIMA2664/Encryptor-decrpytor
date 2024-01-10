
def crypt_key (crypt, action=1):
    # converter[0] tells if it is encrypting (1) or decrypting (-1)
    # converter [1] is the public/private key
    # converter [2] is the n used in RSA
    converter =[]

    if action == 1:
        Type = 'public'

    elif action == -1:
        Type = 'private'

    key_str = input (f"Insert the first number of the {Type} key ")
    key = int (key_str)
    converter.append(key)

    n_str = input (f"Insert the second number of the {Type} key ")
    n = int (n_str)
    converter.append(n)

    # new_crypt is the encrypted version of crypt
    new_crypt = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # if crypt is a string, it converts it to number, then encrypts it
    if type (crypt) is str:

        for char in crypt:
            if not char.isalpha():
                print ("crypt is invalid")
                break

            else:
                num = alphabet.find(char)
                new= RSA_crypt (num, converter)
                new_crypt.append(new)

    #if crypt is an array of numbers, it is directly encrypted
    else:
        for num in crypt:
            if type (num) is int:
                new= RSA_crypt (num, converter)
                new_crypt.append(new)

            else:
                print ("crypt is invalid")
                break

#if crypt is something else, it will print "crypt is invalid"

    return new_crypt


# RSA_crypt produces offset after going through RSA encryption
def RSA_crypt (offset, crypt):
    new_offset = (offset ** crypt [0]) % crypt [1]
    return new_offset




#crypt_key ("python", 1)
#crypt_key ([731, 1643, 72], -1)