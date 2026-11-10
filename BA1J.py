# Find Frequent Words with Mismatches and Reverse Complements

from itertools import product

def hamming_distance(pattern1, pattern2):
    mismatch = 0

    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            mismatch += 1

    return mismatch

def reverse_complement(pattern):

    complement = ""

    for nucleotide in pattern:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'

    return complement[::-1]


text = input()
k = int(input())
d = int(input())    
n = len(text)

patterns = [''.join(p) for p in product('ACGT', repeat=k)]

count = {}
for pattern in patterns:
    total = 0

    rc = reverse_complement(pattern)

    for i in range(n-k+1):
        kmer = text[i:i+k]

        mismatch1 = hamming_distance(pattern, kmer)
        mismatch2 = hamming_distance(rc, kmer)

        if mismatch1 <= d:
            total += 1

        if mismatch2 <= d:
            total += 1

    count[pattern] = total


max_count = max(count.values())

for pattern in count:
    if count[pattern] == max_count:
        print(pattern, end=' ')