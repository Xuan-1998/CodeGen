import sys
from math import comb
input = sys.stdin.readline

def solve():
    n, m_count = map(int, input().split())
    dp = [[0] * (m_count + 1) for _ in range(n + 1)]
    
    # base case: one way to create an empty array
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(min(i, m_count) + 1):
            for k in range(i):
                dp[i][j] += dp[k][min(j, k)] * comb(i - k - 1, j - min(j, k))
    
    print(dp[n][m_count])

if __name__ == "__main__":
    solve()
