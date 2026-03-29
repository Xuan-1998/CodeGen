import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dp = [[0] * (2**n) for _ in range(n+1)]

    # Initialize base case: probability of setting signal powers is 1 when there are no towns
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(2**i):
            if j % 2 == 0:
                dp[i][j] = (dp[i-1][j//2] + dp[i-1][(j//2)+1]) // 2
            else:
                dp[i][j] = 1

    ans = dp[n][-1]
    print(ans)
