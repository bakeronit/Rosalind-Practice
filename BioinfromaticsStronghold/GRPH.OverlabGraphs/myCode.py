filename = 'rosalind_grph.txt' 
seq = {}
with open(filename,'rt') as fh:
    for line in fh:
        line = line.rstrip()
        if line.startswith('>'):
            seq_now = line
            seq[seq_now]=''
        else:
            seq[seq_now] += line
head = {}
tail = {}
for id in seq:
    prefix = seq[id][:3]
    suffix = seq[id][-3:]
    if not prefix in head:
        head[prefix]=[id]
    else:
        head[prefix].append(id)
    if not suffix in tail:
        tail[suffix]=[id]
    else:
        tail[suffix].append(id)

out = open('out.txt','wt')
for su in tail:
    con = []
    if su in head:
        con.append(tail[su])
        con.append(head[su])
        for node in con[0]:
            for node2 in con[1]:
                if not node == node2:
                    print('%s %s'%(node[1:],node2[1:]),file =out)

