# Find Frequent Words with Mismatches and Reverse Complements

def hamming_distance(pattern1, pattern2):
    mismatch = 0

    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i]:
            mismatch += 1

    return mismatch


def neighbors(pattern, d):
    if d == 0:
        return {pattern}

    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood


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

freq = {}
cache = {}

for i in range(len(text) - k + 1):
    kmer = text[i:i+k]

    if kmer not in cache:
        cache[kmer] = neighbors(kmer, d)

    for pattern in cache[kmer]:
        rc = reverse_complement(pattern)

        freq[pattern] = freq.get(pattern, 0) + 1
        freq[rc] = freq.get(rc, 0) + 1


max_count = max(freq.values())

for pattern, count in freq.items():
    if count == max_count:
        print(pattern, end=" ")