import sys

def main():
    T = int(input())
    
    for _ in range(T):
        n, q = map(int, input().split())
        s = list(map(lambda x: 1 if x == "+" else -1, input()))
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] != s[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        
        total_removals = 0
        for _ in range(q):
            l, r = map(int, input().split())
            total_removals += min(dp[r][n], dp[n][r])
        
        print(total_removals)

if __name__ == "__main__":
    main()
