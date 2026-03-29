import sys
from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input().strip())

    dp = [[[] for _ in range(len(t)+1)] for _ in range(len(t)+1)]
    last_pos = [-1] * len(s)
    for i in range(1, len(t)+1):
        for j in range(i+1):
            if t[j:i] in s:
                for k in range(n):
                    if s[k] == t[j:i]:
                        last_pos[k] = i
                        break

    m = float('inf')
    for i in range(1, len(t)+1):
        for j in range(i+1):
            if dp[i][j]:
                continue
            if i > 0 and j > 0:
                prev_m = m
                m = min(m, prev_m + (i-j))
            else:
                m = max(m, i)

    if m == float('inf'):
        return -1

    ans = []
    last_idx = len(t)
    for _ in range(m):
        cur_max = 0
        cur_idx = None
        for i in range(len(s)):
            if s[i] and last_pos[i] > cur_max:
                cur_max = last_pos[i]
                cur_idx = i
        ans.append((cur_idx, last_idx))
        last_idx = cur_max

    print(m)
    for a in ans:
        print(*a)

solve()
