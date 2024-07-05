import sys
from math import gcd

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if 1 in a:
        print(n - a.count(1))
        return
    dp = [[0]*n for _ in range(n)]
    ans = float('inf')
    for i in range(n):
        dp[i][i] = a[i]
        for j in range(i+1, n):
            dp[i][j] = gcd(dp[i][j-1], a[j])
            if dp[i][j] == 1:
                ans = min(ans, j - i)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans + n - 1)

if __name__ == "__main__":
    solve()

