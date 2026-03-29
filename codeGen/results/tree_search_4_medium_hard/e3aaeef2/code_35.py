import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        dp = [[0] * (m + 1) for _ in range(11)]  # dp[i][j] is the length of the resulting number after j operations on a number with i digits
        for i in range(1, 11):
            dp[i][0] = i
        for j in range(1, m + 1):
            for i in range(min(j+1, 10), 0, -1):
                dp[i][j] = min(dp[k][j-1] + (k != i) for k in range(i))
        print((dp[n][m]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
