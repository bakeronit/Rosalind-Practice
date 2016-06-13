#coding-utf-8
from urllib.request import urlopen
filename='rosalind_mprt.txt'
def getFasta(id):
    url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(id)
    fasta = urlopen(url).read().decode("utf-8")
    return fasta

def findMotif(fa):
    l = fa.split('\n')
    del l[0]
    seq = ''.join(l)
    for index in [i for i,x in enumerate(list(seq)) if x == 'N']:
        if seq[index+1] == 'P':
            continue
        if not seq[index+2] in ['S','T']:
            continue
        if seq[index+3] == 'P':
            continue
        else:
            yield index+1

with open(filename,'rt') as fh:
    for line in fh:
        line = line.rstrip()
        fasta = getFasta(line)
        beg = 0
        for id in findMotif(fasta):
            if beg == 0:
                print(line)
                beg = 1
            print(id,end = ' ')
        if beg == 1:
            print()

