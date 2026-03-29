import sys

def palindrome_partition(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if s[j:i+1] == s[j:i+1][::-1]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][i] + 1)
                
    return dp[n][0]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    print(palindrome_partition(s))
