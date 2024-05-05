code
n = int(input())
m = int(input())
MOD = 10**9 + 7

def dfs(n, m):
    if n == 1:
        return 1
    res = 0
    for x in range(m+1):
        res += (pow(2, m-x-1, MOD) * dfs(n-1, m-x)) % MOD
    return res

print(dfs(n, m))
