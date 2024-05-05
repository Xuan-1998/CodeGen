import sys

def steady_tables(N, M):
    # Initialize a dictionary to store the number of ways to distribute the elements
    dp = {0: 1}

    for _ in range(N):
        new_dp = {}
        for i in range(M+1):
            for prev_sum in sorted(dp.keys()):
                # Calculate the new sum and check if it's within bounds
                new_sum = prev_sum + i
                if 0 <= new_sum <= M:
                    new_dp[new_sum] = new_dp.get(new_sum, 0) + dp[prev_sum]
        dp = new_dp

    # Calculate the number of steady tables modulo 1 000 000 000
    total_tables = sum(dp.values()) % (10**9+7)

    return total_tables

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(steady_tables(N, M))
