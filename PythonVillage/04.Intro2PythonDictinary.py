#coding-utf-8
filename = 'rosalind_ini6.txt'
fh = open(filename,'rt')
dict_s = {}
strings = fh.readline().split()
for s in strings:
    dict_s[s] = 1 if not s in dict_s else dict_s[s] + 1

for s in dict_s:
    print('%s %d'%(s,dict_s[s]))
