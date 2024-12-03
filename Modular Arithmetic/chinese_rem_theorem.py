#In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.
from sys import modules

from sympy.ntheory.modular import crt

#Find integer a such that x = a mod 935
moduli = [5, 11, 17]
remainders = [2, 3, 5]

# Using SymPy's crt function
result = crt(moduli, remainders)

ans = result[0] % 935

print(ans)