n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

def recursive_dp(i):
    if i == n:
        return 0
    if dp[i]:
        return dp[i]
    
    max_score = 0
    for k in range(i+1, n):
        if a[k] == a[i] + 1 or a[k] == a[i] - 1:
            max_score = max(max_score, recursive_dp(k))
    
    dp[i] = max(max_score + (n - i), recursive_dp(i-1)) if i > 0 else 0
    return dp[i]

print(recursive_dp(0))
