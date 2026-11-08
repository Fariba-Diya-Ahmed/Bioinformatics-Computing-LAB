# Find All Approximate Occurrences of a Pattern in a String

pattern = input()
dna = input()
d = int(input())

n = len(dna)
k = len(pattern)

for i in range(n-k+1):
    dna2 = dna[i: i+k]

    mismatch = 0
    for j in range(k):
        if(dna2[j] != pattern[j]):
            mismatch += 1

    if mismatch <= d:
        print(i, end=" ")
