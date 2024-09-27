import sys

def longest_increasing_subsequence(pi):
    n = len(pi)
    dp = [1] * n  
    prev = [-1] * n  
    
    for i in range(1, n):
        for j in range(i):
            if pi[j] < pi[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    lis_length = max(dp)
    lis_index = dp.index(lis_length)
    
    lis = []
    while lis_index != -1:
        lis.append(pi[lis_index])
        lis_index = prev[lis_index]
    
    lis.reverse() 
    return lis

def longest_decreasing_subsequence(pi):
    n = len(pi)
    dp = [1] * n  
    prev = [-1] * n 
    
    # Compute the LDS dp table
    for i in range(1, n):
        for j in range(i):
            if pi[j] > pi[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    lds_length = max(dp)
    lds_index = dp.index(lds_length)
    
    lds = []
    while lds_index != -1:
        lds.append(pi[lds_index])
        lds_index = prev[lds_index]
    
    lds.reverse()  
    return lds

def find_lis_and_lds(n, pi):
    lis = longest_increasing_subsequence(pi)
    lds = longest_decreasing_subsequence(pi)
    return lis, lds

#n = 5
#pi = [5,1,4,2,3]
lines = open(sys.argv[1],'rt').readlines()
n = int(lines[0].strip())
pi = [int(i) for i in lines[1].strip().split()]
lis, lds = find_lis_and_lds(n, pi)
print(" ".join([str(i) for i in lis]))
print(" ".join([str(i) for i in lds]))
