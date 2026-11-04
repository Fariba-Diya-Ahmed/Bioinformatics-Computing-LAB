# Find Patterns Forming Clumps in a String

dna = input()
n = len(dna)

k = int(input())    # length of pattern to be found
L = int(input())    # length of window
t = int(input())    # minimum number of times pattern must appear in window

total_windows = n-L+1

most_freq_kmer = set()

for i in range(total_windows):
    window = dna[i:i+L]

    freq = {}

    for j in range(L-k+1):
        kmer = window[j:j+k]

        if kmer in freq:
            freq[kmer] += 1
        else:
            freq[kmer] = 1
            
    for key,value in freq.items():
        if( value >= t):
            most_freq_kmer.add(key)

print(*most_freq_kmer)