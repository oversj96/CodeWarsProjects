# Solution 1
def DNA_strand(dna):
    given_side = list(dna)
    set_one = ['A', 'G', 'T', 'C']
    set_two = ['T', 'C', 'A', 'G']
    return_side = ""
    for i in given_side:
        return_side = return_side + (set_two[set_one.index(i)])
    return return_side

# Solution 2 - roughly the same speed
def DNA_strand2(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

# Test
print(DNA_strand2("ATTGC"))

