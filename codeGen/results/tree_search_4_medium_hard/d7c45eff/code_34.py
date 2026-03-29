import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = [s[:i-1]] * (k+1)
        for j in range(1, min(i, k)+1):
            if j < i:
                dp[i][j].append(dp[i-1][j-1] + [s[i-1]])  # duplicate s[:i-1]
                dp[i][j].append(dp[i-1][j] + [s[i-1]])     # delete the last character of s[:i]
            else:
                dp[i][j].append(dp[i-1][j])   # if j >= i, just copy from dp[i-1][j]

    print(min([''.join(x) for x in dp[n][k]]))

if __name__ == "__main__":
    solve()
