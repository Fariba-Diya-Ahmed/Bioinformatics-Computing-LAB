# Find the Reverse Complement of a String

dna = input()

reverse_dna = dna[::-1] # reverse the dna string

for ch in reverse_dna:
    if ch == 'A':
        print('T',end="")
    elif ch == 'T':
        print('A',end="")
    elif ch == 'C':
        print('G',end="")
    else:
        print('C',end="")

