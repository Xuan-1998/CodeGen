import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: empty tree
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if values[i - 1] == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                for child in range(1, i):
                    if values[child - 1] ^ values[i - 1] == 0 and dp[child - 1][j - 1]:
                        dp[i][j] = 1
                        break
                else:
                    dp[i][j] = 0

    for i in range(n, 0, -1):
        if dp[i][k]:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()
