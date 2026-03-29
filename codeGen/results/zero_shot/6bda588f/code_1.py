import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min(dp[i-1], a[i-1])
        print(min([dp[i] * x + y * (a[n-1] - dp[i]) for i in range(n)]))

if __name__ == "__main__":
    solve()
