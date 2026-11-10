# Compute the number of times a pattern appears in a text

dna = input()
kmer = input()

n = len(dna)
k = len(kmer)

count =0

for i in range(n-k+1):
    if(dna[i:i+k] == kmer):
        count += 1

print(count)