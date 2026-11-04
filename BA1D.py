# Find all occurerences of a pattern in a string

pattern = input()
k = len(pattern)
dna = input()
n = len(dna)

for i in range(n-k+1):
    if(pattern == dna[i:i+k]):
        print(i, end=" ")
