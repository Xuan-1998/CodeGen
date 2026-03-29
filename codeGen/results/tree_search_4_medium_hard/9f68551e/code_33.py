import sys

def solve():
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n):
        if all(k[i] != j for j in range(i)):
            dp[i] = min(dp[i-1], h[i-1]) + 1
        else:
            dp[i] = dp[i-1]

    print(min(h) + dp[-1])

if __name__ == "__main__":
    solve()
