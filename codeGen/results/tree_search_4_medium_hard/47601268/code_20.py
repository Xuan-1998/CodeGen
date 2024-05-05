import sys

def solve(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if bin(i)[2:].count('11') == 0:
            dp[i] = 2 * dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solve(n))
