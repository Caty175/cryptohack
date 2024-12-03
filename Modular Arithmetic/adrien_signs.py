from pydoc import plain, plaintext

from sympy.printing.cxx import reserved

a = 288260533169915
p = 1007621497415251

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

ans = [...]
print(decrypt_flag(ans))