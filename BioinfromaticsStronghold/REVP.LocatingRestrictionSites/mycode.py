
import sys
sys.path.insert(0,'../')
import util

comp = {"A":"T","G":"C","T":"A","C":"G","N":"N"}
def reverseComplement(seq):
    revSeq = ""
    for nt in seq:
        revSeq = comp[nt] + revSeq
    return revSeq

def isRevPal(seq):
    if reverseComplement(seq) == seq:
        return True
    return False

def findRestrictionSites(fasta, length = 12):
    out = open('out.txt','at')  # # FIXME: need to delete outfile every time
    for i in range(len(fasta)):
        for j in range(4,length + 1):
            if i + j > len(fasta):
                break
            seq = fasta[i:i + j]
            if isRevPal(seq):
                print("%d %d"%(i + 1, j),file = out)


fasta = util.readSingleFastaFile("rosalind_revp.txt")
findRestrictionSites(fasta)
