from sys import stdin

def f(i, k, h):
    if i == 0:
        return 0
    if dp[i]:
        return dp[i]
    res = float('inf')
    for j in range(1, i+1):
        if k[j-1] <= j:
            res = min(res, f(k[j-2], k, h) + (j - k[j-2]) + 1)
        else:
            res = min(res, f(j-1, k, h) + 1)
    dp[i] = res
    return res

n = int(stdin.readline())
k = [int(x) for x in stdin.readline().split()]
h = [int(x) for x in stdin.readline().split()]
dp = [0]*(n+1)

res = f(n, k, h)
print(res)
