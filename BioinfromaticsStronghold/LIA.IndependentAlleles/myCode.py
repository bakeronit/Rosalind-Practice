def binomial(n, k):
    """Compute n factorial by a direct multiplicative method."""
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum

(k,N) = (6,18)
def pro(k,n):
    return binomial(2**k,n)*0.25**n*0.75**(2**k-n)

def problem(k,N):
    return 1 - sum([pro(k,n) for n in range(N)])

print(round(problem(k,N),3))
