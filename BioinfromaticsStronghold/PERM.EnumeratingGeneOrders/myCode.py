#coding-utf-8
def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]

n = 7
out = open('out.txt','wt')
sm=1
for i in range(1,n+1):
    sm*=i
print(sm,file = out)
for p in permute([m for m in range(1,n+1)]):
    p = [str(i) for i in p]
    print(' '.join(p),file=out)
