import sys

def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    return n, a, b, c

def solve(n, a, b, c):
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        if i == 1:
            dp[i][0] = a[0]
            dp[i][1] = max(a[0], b[0])
        else:
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = c[i-1] + (dp[i-1][0] if i > 1 else 0)
                elif j == 1:
                    dp[i][j] = b[i-1] + max(dp[i-1][0], dp[i-1][1])
                else:
                    dp[i][j] = a[i-1] + max(dp[i-1][0], dp[i-1][1])

    return dp[n][1]

if __name__ == "__main__":
    n, a, b, c = read_input()
    print(solve(n, a, b, c))
