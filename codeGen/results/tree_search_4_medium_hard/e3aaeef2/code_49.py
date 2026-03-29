code
import sys

def solve():
    t = int(input())
    memo = {}
    for _ in range(t):
        n, m = map(int, input().split())
        if (n, m) not in memo:
            dp = [[0]*(m+1) for _ in range(10**9+7)]
            dp[0][0] = 1
            for i in range(1, n+1):
                for j in range(m+1):
                    if j == 0:
                        dp[i][j] = min(9, len(str(i)))
                    else:
                        dp[i][j] = min(dp[int(str(i)[0]) + 1], dp[(i%10)+1])
            memo[(n, m)] = dp[n][m]
        print(memo[(n, m)], file=sys.stdout)

if __name__ == "__main__":
    solve()
