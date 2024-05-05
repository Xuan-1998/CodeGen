from collections import defaultdict

def solve():
    n = int(input())
    s = input()

    # Initialize DP table
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Calculate prefix sums
    ps = [0]
    for c in s:
        ps.append(ps[-1] | int(c))

    # Fill DP table
    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[i][j] = max(dp[i-1][k] | (ps[j]-ps[k]) for k in range(i-1, j))

    return bin(max([dp[i][n] for i in range(n)]))[2:]

if __name__ == "__main__":
    print(solve())
