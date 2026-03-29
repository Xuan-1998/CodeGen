import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[sys.maxsize for _ in range(k)] for _ in range(n)]

    for i in range(k):
        if s[i] == 'R':
            dp[0][i] = 1
        elif s[i] == 'G':
            dp[0][i] = 2
        else:
            dp[0][i] = 3

    for i in range(1, n):
        for j in range(min(i, k-1), -1, -1):
            if s[j+i-k+1] == 'R':
                dp[i][j] = min(dp[i-1][min(j, k-1)] + 1, dp[i-1][j])
            elif s[j+i-k+1] == 'G':
                dp[i][j] = min(dp[i-1][min(j, k-1)] + 2, dp[i-1][j])
            else:
                dp[i][j] = min(dp[i-1][min(j, k-1)] + 3, dp[i-1][j])

    print(min(dp[-1]))

if __name__ == '__main__':
    solve()
