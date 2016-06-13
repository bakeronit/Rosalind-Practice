#coding-utf-8
filename = 'rosalind_ini4.txt'
fh = open(filename,'rt')
line = fh.readline().rstrip().split()
a = int(line[0])
b = int(line[1])
su = 0
for i in range(a,b+1):
    if i % 2 == 1:
        su += i
print(su)
