import sys
from collections import defaultdict

def solution():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        dp = [[0.0 for _ in range(1 << 16)] for _ in range(n + 1)]
        seen = set()
        total_prob = 0
        for i in range(n):
            p, a, b = map(int, sys.stdin.readline().split())
            if (a | b) not in seen:
                seen.add(a | b)
                dp[i+1][a|b] = max(dp[i][a|b], p * dp[i][0])
        total_prob = sum([max(x, 0) for x in dp[n]])
        print('%.6f' % total_prob)

solution()
