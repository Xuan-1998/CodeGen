import sys

def solve(N, K, Arr):
    dp = [0] * N
    max_val_seen_so_far = 0

    for i in range(N):
        if Arr[i] > K:
            max_val_seen_so_far = Arr[i]
            dp[i] = 1
        else:
            if Arr[i] <= max_val_seen_so_far:
                dp[i] = dp[i-1] if i > 0 else 0
            else:
                max_val_seen_so_far = Arr[i]
                dp[i] = dp[i-1] + (dp[i-1] if i > 0 else 0)

    return sum(dp)

# Read input from stdin
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

print(solve(N, K, Arr))
