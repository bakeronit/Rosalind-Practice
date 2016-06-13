#coding-utf-8
from numpy import *
filename = 'rosalind_iev.txt'
fh=open(filename,'rt')
line = fh.readline().rstrip()
n = line.split()
n = [int(i) for i in n]
possible = array([1,1,1,3/4,1/2,0])
parents = array(n)
print(parents)
print(sum(parents*possible)*2)
