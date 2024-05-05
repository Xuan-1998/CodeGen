import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if signs[i - 1] == '+':
            dp[0][i] += 1
        else:
            dp[0][i] -= 1

    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if signs[left] == '+':
                dp[left][right] += 1
            else:
                dp[left][right] -= 1

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[l-1][r], dp[0][r-l+1]))

if __name__ == "__main__":
    solve()
