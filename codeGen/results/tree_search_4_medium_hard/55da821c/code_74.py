from io import StringIO
import sys

def solve():
    n = int(input())
    m = int(input())
    plants = []
    for _ in range(n):
        s, x = map(int, input().split())
        plants.append((s, x))
    
    dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for last_s in range(1, m + 1):
            for species in range(i):
                if not plants[species - 1][0] == last_s:
                    dp[i][last_s][i] = min(dp[i][j][i - 1] + abs(plants[species - 1][1]) - plants[species - 2][1] for j in range(1, m))
    
    ans = float('inf')
    for i in range(m):
        if dp[m][m][i] < ans:
            ans = dp[m][m][i]
    
    print(ans)

if __name__ == "__main__":
    solve()
