from sys import stdin

def solve():
    n, k = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    
    dp = [["" for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = "a" * i
    for j in range(k+1):
        dp[0][j] = ""
    
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if j == 1:
                dp[i][j] = s[i-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], s[i-1:j-1] + (s[j-1] if i >= j else ""))
    
    print(dp[n][k])

if __name__ == "__main__":
    solve()
