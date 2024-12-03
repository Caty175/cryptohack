import math

#https://hackmd.io/@ADP/r1JV8qFk0?utm_source=preview-mode&utm_medium=rec#Cryptohack-MODULAR-ARITHMETIC

#Using Euclid's algorithm
print(math.gcd(66528, 52920))

#Extended Euclid's algorithm
#Using the two primes p = 26513, q = 32321, find the integers u,v such that
#p * u + q * v = gcd(p,q)

def egcd(a, b) :
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

gcd, u, v =egcd(26513, 32321)
print(min(u, v))