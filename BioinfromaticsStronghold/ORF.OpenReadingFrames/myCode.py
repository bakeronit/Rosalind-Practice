#coding-utf-8
import re
reverse = {'A':'T','T':'A','C':'G','G':'C'}
start = ['ATG']
stop = ['TAG','TGA','TAA']

def translate(orf):
    codon = {}
    with open('../codons.txt','rt') as fh:
        for line in fh:
            line = line.strip().split()
            codon[line[0]] = line[1]
    pro = ''
    for i in range(0,len(orf)+1,3):
        aa = codon[orf[i:i+3]]
        if aa == 'Stop':
            return pro
        else:
            pro += aa

def getReverse(seq):
    r_seq = ''
    for nt in seq:
        r_seq = reverse[nt] + r_seq
    return r_seq

def findOrf(seq):
    protein = []
    for span in [i.span() for i in re.finditer('ATG',seq)]:
        (beg,_) = span
        for index in range(beg,len(seq)+1,3):
            if not seq[index:index+3] in stop:
                continue
            else:
                end = index + 3
                orf = seq[beg:end]
                protein.append(translate(orf))
                break
    return protein

filename='rosalind_orf.txt'
seq = ''
with open(filename,'rt') as fh:
    for line in fh:
        if line.startswith('>'):
            continue
        else:
            seq += line.strip()
f=findOrf(seq)
b=findOrf(getReverse(seq))
f.extend(b)
final=list(set(f))
for i in final:
    print(i)
