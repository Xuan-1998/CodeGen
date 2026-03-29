import sys

def solve():
    n = int(input())
    monsters = list(map(int, input().split()))
    healths = list(map(int, input().split()))

    dp = [[0] * 10**9 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(monsters[i-1]):
            dp[i][j] = sys.maxsize
        for j in range(monsters[i-1], 10**9):
            if j >= monsters[i-1]:
                dp[i][j] = min(dp[i-1][monsters[i-2]] + healths[i-1], dp[i][max(0, j-monsters[i-1]+1)])
            else:
                dp[i][j] = dp[i][max(0, j-monsters[i-1]+1)]

    return str(min(dp[n]))

if __name__ == "__main__":
    print(solve())
