import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        left_moves = [0] * (n + 1)
        
        for i in range(1, n + 1):
            for j in range(min(i, k) + 1):
                if j == 0:
                    dp[i][j] = arr[i - 1]
                else:
                    if left_moves[i - 1] < z:
                        dp[i][j] = max(dp[i - 1][j - 1] + arr[i - 1], dp[i - 1][j])
                    else:
                        dp[i][j] = dp[i - 1][j]
                if j > 0 and left_moves[i - 2] < z:
                    left_moves[i - 1] = j
                else:
                    left_moves[i - 1] = max(left_moves[i - 2], j)
        
        print(max(dp[n]))

if __name__ == "__main__":
    solve()
