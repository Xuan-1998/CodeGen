from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    s = list(input())

    dp = defaultdict(int)
    dp[0] = 0

    for i in range(1, n+1):
        if s[i-1] == '+':
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] - 1

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[r] - dp[l-1], abs(r-l)))

if __name__ == '__main__':
    solve()
