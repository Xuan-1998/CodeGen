from math import comb

def dfs(i):
    if i in memo: return memo[i]
    res = (res + comb(C-i, k) * (k+1) ** (C-k)) % (10**9+7)
    for k in range(0, min(i+1, C)+1):  # handle cases where N or M is 0
        if k > i: break
        res = (res + comb(C-i, k-1) * (k) ** (C-k)) % (10**9+7)
    memo[i] = res; 
    return res;

memo = {0: 1}; 
dp = [0]*(C+1); 
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(C+1):  # handle cases where N or M is 0
        if i == 0: 
            dp[i] = 1;  # base case: one way to build a sequence with no spheres
        elif i == C:
            dp[i] = 1;  # base case: one way to build the entire sequence
        else:
            dp[i] = dfs(i); 
    print(*dp, sep=' ')
