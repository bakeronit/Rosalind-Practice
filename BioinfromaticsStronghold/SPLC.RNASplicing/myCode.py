
codon = {}
with open("../codons.txt","rt") as fh:
    for line in fh:
        line = line.strip()
        c,a = line.split()
        codon[c] = a

def getCDS(seq,introns):
    for intron in introns:
        start = seq.find(intron)
        seq = seq[:start] + seq[start + len(intron):]
    return seq

def translate(cds):
    pep = ""
    for i in range(int(len(cds)/3)):
        aa = codon[cds[0 + i*3 : 3 + i*3]]
        if aa == "Stop":
            break
        pep += aa
    return pep

with open("rosalind_splc.txt","rt") as fh:
    l = 0
    t = ""
    introns = []
    for line in fh:
        line = line.strip()
        if line.startswith(">"):
            l += 1
            continue
        elif l == 1:
            t += line
        elif l > 0:
            introns.append(line)

out = open("out.txt","wt")
cds = getCDS(t,introns)
print(translate(cds),file = out)
