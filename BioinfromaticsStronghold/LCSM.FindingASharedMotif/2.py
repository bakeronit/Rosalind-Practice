#coding-utf-8
import sys
filename = 'rosalind_lcsm.txt'
seq = {}
with open(filename,'rt') as fh:
    for line in fh:
        line = line.rstrip()
        if line.startswith('>'):
            id = line[1:]
            seq[id] = ''
        else:
            seq[id] += line

minlen = 1001
minid = ''
for id in seq:
    (minlen,minid) = (len(seq[id]),id) if len(seq[id]) < minlen else (minlen,minid)

smallSeq = seq[minid]
print('short seq is %s'%smallSeq)
for l in range(1,minlen+1):
    f = 0
    for i in range(minlen-l+1):
        motif = smallSeq[i:i+l]
        print('start from motif %s'%motif)
        sub_get = True
        for id in seq:
            if seq[id].find(motif) == -1:
                sub_get = False
        if sub_get == True:
            ok_motif = motif
        else:
            f += 1
    if f == minlen-l+1:
        print(ok_motif) 
        sys.exit(1)
