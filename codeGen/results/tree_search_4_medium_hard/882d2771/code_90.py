t, l, r = map(int, input().split())
mod = 10**9 + 7

# Initialize dp with base cases: f(1, k) = k for 0 ≤ k ≤ t
dp = {}
for k in range(t+1):
    dp[(1, k)] = k

def f(S):
    r, k = S
    if (r, k) in dp:
        return dp[(r, k)]
    
    res = float('inf')
    for g in range(1, r+1):
        res = min(res, f((g, k)) + f((r-g, 0)))
        
    dp[(r, k)] = res
    return res

print(f((l, t)) % mod)
