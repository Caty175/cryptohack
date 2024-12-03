#In the below list there are two non-quadratic residues and one quadratic residue.
#In the below list there are two non-quadratic residues and one quadratic residue.
#Find the quadratic residue and then calculate its square root.

p = 29
ints = [14, 6, 11]

res = [a for a in range(p) if pow(a, 2, p) in ints ]
print(min(res))