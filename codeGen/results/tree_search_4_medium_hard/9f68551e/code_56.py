import sys

def solve():
    n = int(sys.stdin.readline().strip())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))

    dp = [0] * (max(k) + 1)
    for i in range(n):
        for j in range(min(max(k) + 1), min(k[i], h[i]), -1):
            if j >= h[i]:
                dp[j] = max(dp[j], dp[k[i] - 1] + h[i])

    print(max(dp))

if __name__ == "__main__":
    solve()
