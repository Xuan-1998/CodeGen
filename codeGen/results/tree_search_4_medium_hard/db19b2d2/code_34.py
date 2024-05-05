import sys

def main():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        print(-1)
        return
    
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1.0
    total_players = sum(s[:h])
    
    for i in range(1, m + 1):
        for k in range(n + 1):
            if i < h:
                p = min(k, len(s[i-1])) / n
            else:
                p = total_players / (n - k)
            
            dp[i][k] = 1.0 - (1.0 - p) * (1.0 - dp[i-1][k-1])
    
    print(dp[m][n])

if __name__ == "__main__":
    main()
