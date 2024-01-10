# RSA-private produces the public key using e - the private key, 
# p,q - two prime numbers such that n is the product of the p and q
# RSA_private produces all errors when encountered
# for convenience p is set to 10,007 and q is set to 10,009, but the user can decide to go further
# e is a number coprime to (p-1)(q-1)
def RSA (e, p=10007, q=10009):
    n = (p * q)
    m = ((p - 1) * (q - 1))

    if e < 1 or p < 2 or q < 2:
        print ('All arguments must at least be greater than 2')

    elif not is_prime (p):
        print (f'{p} is not valid because it is not prime')
        
    elif not is_prime (q):
        print (f'{q} is not valid because it is not prime')
        
    elif e >= m :
        print (f'{e} is not valid - must be lower than {m} - (p-1)(q-1)')

    elif type (coprime (e, m)) is not bool:
        factor = coprime (e, m)
        print (f'{e} is not valid because it is not coprime to {m} :(p-1)(q-1) - common factor is {factor}')

    else: 
        action = input ('Do you want the private or public key? ')

        if action == 'private':
            print (f'Private key: ({e}, {n})')
            return [e ,n]
            
        if action == 'public':
            pub_key = public_key (e , m)
            print (f'Public key: ({pub_key}, {n})')
            return [pub_key, n]
            
        else: 
            print ('Action unclear; please choose "private" or "public"')
            return RSA (e, p, q)


# public_key generates a public key - (d *e) is 1 mod m 
# e fulfills all the requirement for RSA encryption when used in RSA
def public_key (a, b, x1 = 0, y1 = 1, x2 = 1, y2 = 0):
    r1 = a*x1 + b*y1
    r2 = a*x2 + b*y2

    if r2 == 1:
        if x2 < 0:
            return (x2 + b)
        
        else: 
            return x2
    
    else:
        # use of extended euclidean algorithm
        multiplier = r1 // r2
        x3 = x1 - x2*multiplier 
        y3 = y1 - y2*multiplier

        x1 = x2
        y1 = y2   
        x2 = x3
        y2 = y3

        return public_key (a, b, x1, y1, x2, y2)




# is_prime produces true if num is a prime number, false otherwise
def is_prime (num):
    # removes all multiples of 2
    if (num % 2) == 0 and num != 2:
        return False
    
    # removes all odd composite number possibilities
    i = 3
    while i < num:
        if (num % i) == 0:
            return False
            
        else: 
            i += 2

    return True

# coprime produces true if x and y are coprime - gcd (x,y) = 1, false otherwise
def coprime (x, y): 
    minimum = min (x,y)
    maximum = max (x,y)

    if minimum == 1:
        return True
    
    elif minimum == 0:
        return maximum
    
    else:
        # uses the exteneded euclidean algorithm to reduce computations
        return coprime (minimum, maximum % minimum)

RSA(13, 19, 2)
#RSA(59992)