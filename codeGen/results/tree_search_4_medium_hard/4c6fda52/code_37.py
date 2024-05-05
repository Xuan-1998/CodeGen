def min_changes(n, k, s):
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i
    
    for j in range(k+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            if s[i-1] != 'RGB'[i%3]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1)
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][k]

def main():
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0: break
        s = input()
        print(min_changes(n, k, s))

if __name__ == "__main__":
    main()
