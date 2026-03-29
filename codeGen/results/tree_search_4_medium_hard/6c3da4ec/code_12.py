from sys import stdin

def solve():
    n = int(stdin.readline())
    s = stdin.readline().strip()

    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1):
            if j-i == 1:
                dp[i][j] = int(s[i-1])
            else:
                dp[i][j] = max(int(s[k-1], 2) | dp[k][j] for k in range(i+1, j))

    print(bin(max(OR(dp[k][n-1], int(s[:k], 2)) for k in range(n))) or '0')

if __name__ == "__main__":
    solve()
