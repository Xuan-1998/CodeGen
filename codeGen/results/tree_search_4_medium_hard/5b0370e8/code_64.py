import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[-1] * (1 << k) for _ in range(n + 1)]

        for i in range(n):
            x = int(input())
            for y in range(1 << k):
                if not (x & y):  # current element doesn't have the property
                    if i > 0:
                        dp[i][y] += dp[i - 1][y]
                else:  # current element has the property
                    if i == n - 1:
                        dp[i][y] = 1
                    elif y + 1 < (1 << k):
                        dp[i][y + 1] += dp[i - 1][y]

        ans = sum(dp[-1])
        print(ans % (10**9 + 7))

if __name__ == '__main__':
    solve()
