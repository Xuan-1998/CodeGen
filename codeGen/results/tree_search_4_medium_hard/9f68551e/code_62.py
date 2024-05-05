import sys

def solve():
    n = int(input())
    max_health = 0
    for _ in range(n):
        k, h = map(int, input().split())
        max_health = max(max_health, k)
    dp = [[-1] * (max_health + 1) for _ in range(n + 1)]

    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if j < i:
                dp[i][j] = max(dp[i-1][k] + k+1 for k in range(j))
            else:
                dp[i][j] = j
    print(max(dp[-1]))

if __name__ == "__main__":
    solve()
