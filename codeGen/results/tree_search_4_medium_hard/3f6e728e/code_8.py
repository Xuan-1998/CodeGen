code
import math

def solve():
    t = int(input())
    for _ in range(t):
        n, m, c = map(int, input().split())
        u = list(map(int, input().split()))
        l = list(map(int, input().split()))
        dp = {0: 1}
        for i in range(1, c+1):
            if i not in dp:
                continue
            dp[i] = (dp.get(i-1, 0) or 0) * sum((dp.get(j, 0) or 0) % (10**9 + 7) for j in l)
        print(*[dp.get(i, 0) % (10**9 + 7) for i in range(c)], sep=' ')

solve()
code
