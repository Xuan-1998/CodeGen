import sys

def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))

    dp = [0] * (N + 1)
    max_val = 0
    for i in range(N):
        max_val = max(Arr[i], max_val)
        if max_val > K:
            dp[i+1] += 1
        else:
            max_val = Arr[i]

    res = sum(dp[:i+1] for i in range(N) if max(Arr[:i+1]) > K)

    print(res)

solve()
