# Find the Most Frequent Words with Mismatches in a String

from itertools import product

def hamming_distance(pattern1, pattern2):
    mismatch = 0

    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            mismatch += 1

    return mismatch

text = input()
k = int(input())
d = int(input())    
n = len(text)

patterns = [''.join(p) for p in product('ACGT', repeat=k)]

count = {}

for pattern in patterns:
    total = 0

    for i in range(n-k+1):
        kmer = text[i:i+k]

        mismatch = hamming_distance(pattern, kmer)

        if mismatch <= d:
            total += 1

    count[pattern] = total

max_count = max(count.values())

for pattern in count:
    if count[pattern] == max_count:
        print(pattern, end=' ')