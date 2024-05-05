import sys

def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(min(i, N) + 1):
                if i > j:
                    dp[i][j] = (dp[i - 1][j] + 10 ** (N - j) * (i - j)) / (2 ** N)
                elif j > i:
                    dp[i][j] = (dp[i][j - 1] + 10 ** (N - i) * (j - i)) / (2 ** N)
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + 10 ** (N - j) * (i - j)) / (2 ** N)
        
        print(sum([dp[i][j] for i in range(N + 1) for j in range(min(i, N) + 1)]))

expected_carries()
