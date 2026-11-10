# Find the Most Frequent Words in a String

dna = input()
k = int(input())

n = len(dna)
freq = {}

for i in range(n-k+1):
    kmer = dna[i:i+k]

    if kmer in freq:
        freq[kmer] += 1
    else:
        freq[kmer] = 1
        
maximum_freq = max(freq.values())

for key,value in freq.items():
    if value == maximum_freq:
        print(key,end=" ")