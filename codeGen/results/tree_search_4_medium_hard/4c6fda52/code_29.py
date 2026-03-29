import sys

def solve():
    n = int(input())
    s = input()
    
    k = 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i + 1, k + 1)):
            if s[i - 1] == 'R':
                dp[i][j] = dp[i-1][j-1] + (s[i-2] != 'G')
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (s[i-1] != 'G')
    
    print(sum(1 for x in dp[n-1] if x > 0))

if __name__ == "__main__":
    solve()
