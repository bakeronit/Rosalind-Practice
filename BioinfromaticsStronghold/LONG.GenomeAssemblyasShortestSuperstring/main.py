def readSequences(filename="rosalind_long.txt"):
    with open(filename,"rt") as fh:
        seq = ""
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                if seq != "":
                    yield seq
                seq = ""
                continue
            else:
                seq += line

## find the overlapped regions between two sequences and return the superstring
def getSuperstring(seq1,seq2):
    superstring = ""
    #min_overlap_len = min(len(seq1),len(seq2)) // 3
    for i in range(10, len(seq1)):
        if seq1[:i] == seq2[len(seq2)-i:]:
            superstring = seq2+seq1[i:]
        if seq2[:i] == seq1[len(seq1)-i:]:
            superstring = seq1+seq2[i:]
    return superstring

def assemble_single_round(sequences, current_superstring):
    target_index = -1 
    shortest_superstring = current_superstring
    for i, seq in enumerate(sequences):
        superstring = getSuperstring(current_superstring, seq)
        if superstring == "":
            continue
        if len(superstring) < len(shortest_superstring) or shortest_superstring == current_superstring:
            shortest_superstring = superstring
            target_index = i
    if not target_index == -1:
        sequences.pop(target_index)
    return [shortest_superstring] + sequences


def main():
    sequences = list(readSequences())

    while len(sequences) > 1:
        print(len(sequences)) ## keep track of the assembly
        sequences = assemble_single_round(sequences[1:], sequences[0])

    return sequences[0]

if __name__ == "__main__":
    print(main())




