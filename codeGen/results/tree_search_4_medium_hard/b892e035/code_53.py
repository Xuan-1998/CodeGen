import sys
from collections import defaultdict

def solve():
    T = int(input())
    dp = defaultdict(lambda: [[0, 0] for _ in range(2)])

    def dfs(i, prev):
        if i >= n:
            return 1
        res = [0, 0]
        for j in range(2):
            p1, num1, num2 = map(int, input().split())
            p2 = (p1 * dp[i-1][j][0] + (1-p1) * dp[i-1][j][1]) / 2
            res[j] = p2
        return res

    for _ in range(T):
        n = int(input())
        for i in range(n):
            p1, num1, num2 = map(int, input().split())
        res = dfs(n-1, -1)
        print(sum(res) / 2)

if __name__ == "__main__":
    solve()
