# Find a Position in a Genome Minimizing the Skew

dna = input()
n = len(dna)

skew = 0
skew_list = [0] 

for i in range(n):
    if(dna[i])== 'G':
        skew += 1
    elif(dna[i])== 'C':
        skew -= 1
    else:
        skew += 0

    skew_list.append(skew)

minimum_skew = min(skew_list)

for i in range( len(skew_list)):
    if(skew_list[i] == minimum_skew):
        print(i, end=" ")

