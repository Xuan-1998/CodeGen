import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        if signs[i - 1] == "+":
            prefix_sum[i] = prefix_sum[i - 1] + 1
        else:
            prefix_sum[i] = prefix_sum[i - 1] - 1

    for i in range(n - 1, -1, -1):
        if prefix_sum[i] > 0:
            dp[i] = min(dp[i], dp[i + 1]) if i < n - 1 else 0
        elif prefix_sum[i] < 0:
            dp[i] = min(dp[i], dp[i + 1]) if i < n - 1 else 0
        else:
            dp[i] = min(dp[i], dp[i + 1]) if i < n - 1 else 0

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[r], dp[l - 1]))

if __name__ == "__main__":
    solve()
