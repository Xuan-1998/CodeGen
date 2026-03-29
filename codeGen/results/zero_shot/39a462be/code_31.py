import sys
from functools import lru_cache

@lru_cache(None)
def lcs_length(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def solve():
    a, b = sys.stdin.readline().split()
    m, n = len(a), len(b)
    
    best_score = 0
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i and j:
                lcs_len = lcs_length(a[:i], b[:j])
                score = 4 * lcs_len - (i + j)
                best_score = max(best_score, score)
    
    print(best_score)

if __name__ == "__main__":
    solve()
