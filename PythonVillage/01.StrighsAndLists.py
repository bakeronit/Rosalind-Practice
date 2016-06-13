#coding-utf-8
filename = 'rosalind_ini3.txt'
fh = open(filename,'rt')
string = fh.readline().rstrip()
index = fh.readline().rstrip()
index = [int(i) for i in index.split()]
print('%s %s'%(string[index[0]:index[1]+1],string[index[2]:index[3]+1]))
