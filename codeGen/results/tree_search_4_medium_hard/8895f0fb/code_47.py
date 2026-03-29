import math

def expected_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            if i == 1:
                dp[i] = 9
            else:
                dp[i] = min(1 + dp[i-1], 9*(i-1))
        
        total_pairs = sum((10**n - 9) for n in range(N+1))
        expected_carries = sum(dp[n] * (10**n - 9) for n in range(N+1)) / total_pairs
        print("{:.6f}".format(expected_carries))

expected_carries()
