import sys

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    
    for n in range(1, N + 1):
        for c in range(min(n, 9 - (n % 10))):
            dp[n][c + 1] = min(dp[n][c] + (n % 10 == 0), 9 - int((n % 10) * 10))
    
    expected_carries = sum([dp[N][c] for c in range(min(N, 9 - int(N % 10)))])
    print(expected_carries / (N ** 2))
