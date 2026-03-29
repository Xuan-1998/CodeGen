from collections import defaultdict

def smallest_string(n, k):
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if j == 1:
                dp[i][j] = [s[:i]]
            else:
                if s[i-1]:
                    dp[i][j] = sorted(dp[i-1][j-1] + [x+y for x in dp[i-1][j-1] for y in [s[i-1], '']])
                else:
                    dp[i][j] = dp[i-1][j]
    
    return min(sorted(dp[n][k]), key=lambda s: (s, len(s)))

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(smallest_string(n, k))
