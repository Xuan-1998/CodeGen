import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[False] * (n+1) for _ in range(n+1)]
    prefix_sum = [0] + [sum(1 if sign == '+' else -1 for sign in signs[:i]) for i in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = (dp[i-1][k] or prefix_sum[i]-prefix_sum[k] >= 0) for k in range(i)
        for j in range(i):
            if prefix_sum[i]-prefix_sum[j] < 0:
                dp[i][j+1] = True

    for _ in range(q):
        l, r = map(int, input().split())
        ans = min(r-l+1, sum(dp[r][k] or not dp[l-1][k] for k in range(min(l, r))))
        print(ans)

if __name__ == "__main__":
    solve()
