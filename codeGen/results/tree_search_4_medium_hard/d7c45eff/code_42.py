{
import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = [['' for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if i == 1:
                dp[i][j] = s[:j]
            elif j < i-1:
                dp[i][j] = min(dp[i-1][j], s[-1] + dp[i-1][j-1], dp[i-1][j-1]) 
            else:
                dp[i][j] = min(dp[i-1][j-1], s[-1] + dp[i-1][j-1])

    print(dp[n][k])
}

if __name__ == "__main__":
    solve()
}
