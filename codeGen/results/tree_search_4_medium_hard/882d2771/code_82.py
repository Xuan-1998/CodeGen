def f(n):
    # You need to implement this function based on the definition of f(n)
    pass

def solve(t, l, r):
    MOD = 10**9 + 7
    dp = [[-1 for _ in range(l+1)] for _ in range(r-l+2)]
    
    for i in range(l, r+1):
        if i == l:
            for j in range(2, l+1):
                dp[i-l][j] = f(j) - min(f(k) + k * (i-k) for k in range(2, j+1))
        
        else:
            for j in range(2, l+1):
                if dp[i-l-1][k] != -1 and i-k > 0:
                    dp[i-l][j] = min(dp[i-l-1][k] + f(i-k) - k * (i-k), dp[i-l][j])
                else:
                    dp[i-l][j] = f(j) - min(f(k) + k * (i-k) for k in range(2, j+1))
    
    total = 0
    for i in range(l, r+1):
        total += t*(dp[i-l][l+1] if dp[i-l][l+1] != -1 else f(l)) % MOD
    
    return (total - l*f(r) + r*f(r) - sum(f(i) for i in range(2, r+1))) % MOD

t = int(input())
l, r = map(int, input().split())

print(solve(t, l, r))
