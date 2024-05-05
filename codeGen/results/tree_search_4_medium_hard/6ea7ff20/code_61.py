import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    dp = [[([], []) for _ in range(n+1)] for _ in range(2*n+1)]

    for i in range(1, 2*n+1):
        for j in range(min(i//2, n), -1, -1):
            if p[i-1] < dp[i-j][j][0][-1]:
                dp[i][j] = (dp[i-j][j][0] + [p[i-1]], [])
            elif p[i-1] > dp[i-j][j][0][-1]:
                dp[i][j] = ([], dp[i-j][j][1] + [p[i-1]])
            else:
                if not dp[i-j][j][0]:
                    dp[i][j] = (dp[i-j][j][0] + [p[i-1]], [])
                elif not dp[i-j][j][1]:
                    dp[i][j] = ([], dp[i-j][j][1] + [p[i-1]])

    if len(dp[-1][-1][0]) == n and len(dp[-1][-1][1]) == n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
