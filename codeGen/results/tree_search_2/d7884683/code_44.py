import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [[0] * (n // 2 + 1) for _ in range(n)]
        
        left_sum = sum(arr[:i+1]) for i in range(n)
        right_sum = sum(arr[i:]) for i in range(n)

        for i in range(1, n):
            for j in range(min(i, n//2), -1, -1):
                if left_sum[j] == right_sum[i-j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) if j > 0 else 0

        print(max(max(row) for row in dp))

if __name__ == "__main__":
    solve()
