from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))

def decrypt_flag(ans):
    plaintext = []
    for i in ans:
        if pow(i, (p - 1) // 2, p) == 1:
            plaintext.append('1')
        else:
            plaintext.append('0')
    plaintext = ''.join(plaintext)
    reversed(plaintext)
    plaintext =''.join([chr(int(plaintext[i:i +8], 2))for i in range(0, len(plaintext), 8) ])
    return plaintext

ans = encrypt_flag(FLAG)
print(decrypt_flag(ans))
