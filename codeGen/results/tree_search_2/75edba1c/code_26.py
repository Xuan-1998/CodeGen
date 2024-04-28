from sys import stdin

def solve():
    N, K = map(int, stdin.readline().split())
    Arr = list(map(int, stdin.readline().split()))

    dp = [[0] * (K + 1) for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            if Arr[j] > K:
                dp[i][Arr[j]] += 1
    return sum(dp[i][K] for i in range(N))

print(solve())
