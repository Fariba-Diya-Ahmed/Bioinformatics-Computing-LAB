# Find the Most Frequent Words with Mismatches in a String

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


text = input()
k, d = map(int, input().split())

n = len(text)

freq = {}

for i in range(n-k+1):

    kmer = text[i:i+k]

    for neighbor in neighbors(kmer, d):

        if neighbor not in freq:
            freq[neighbor] = 1

        else:
            freq[neighbor] += 1


max_count = max(freq.values())

for pattern in freq:

    if freq[pattern] == max_count:
        print(pattern, end=' ')