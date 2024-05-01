def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(n):
        if i == 0:
            dp[i] = 1
        else:
            for k in range(i, -1, -1):
                if k > 0 and k < n-1 and sequence[k] == sequence[i]:
                    dp[i] = max(dp[i], dp[k-1] + (i-k+1))
                elif k == i:
                    break
    return dp[-1]

print(solve())
