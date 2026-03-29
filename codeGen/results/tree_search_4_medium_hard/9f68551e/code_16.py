import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = list(map(int, input().split()))
        h = list(map(int, input().split()))
        
        dp = [[0] * (max(k) + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(max(k[:i]) + 1):
                if j < k[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1].max(0, j - k[i - 1]) + h[i - 1], dp[i][j])
        
        print(min(dp[-1]))

if __name__ == "__main__":
    main()
