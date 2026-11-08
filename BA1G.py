# Compute the Hamming Distance Between Two Strings

dna1 = input()
dna2 = input()

n = len(dna1)
mismatch = 0

for i in range(n):
    if (dna1[i]!= dna2[i]):
        mismatch += 1

print(mismatch)
