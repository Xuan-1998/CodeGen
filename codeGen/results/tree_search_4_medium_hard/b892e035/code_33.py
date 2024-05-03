import sys
from math import comb

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probs = [list(map(int, input().split())) for _ in range(n)]
        dp = [[0.0] * 2 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(2):
                if i == 1:
                    dp[i][j] = probs[0][j]
                else:
                    dp[i][j] = (dp[i - 1][0] * probs[i - 1][0] / comb(i, 1) + 
                                 dp[i - 1][1] * probs[i - 1][1] / comb(i, 1))
        print('%.6f' % sum(dp[-1]))

if __name__ == "__main__":
    solve()
