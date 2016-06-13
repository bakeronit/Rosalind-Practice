#coding-utf-8
filename = 'rosalind_ini5.txt'
i = 1
with open(filename,'rt') as fh:
    for line in fh:
        if i % 2 == 0:
            print(line.rstrip())
        i += 1

