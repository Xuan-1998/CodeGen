import sys
from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s_list = [input().strip() for _ in range(n)]

    dp = [{} for _ in range(len(t) + 1)]
    used = set()

    res = []
    min_steps = float('inf')

    for i, s in enumerate(s_list):
        j = len(s) - 1
        while j < len(t) and t[j] == s[-1]:
            dp[j+1][s] = dp[j][get(s)] + 1
            used.add((i, j))
            j -= 1

    for i in range(len(t)):
        if not dp[i]:
            return -1

        cur_dp = dp[i]
        min_steps_i = float('inf')
        prev_s = None

        for s, cnt in sorted(cur_dp.items(), key=lambda x: (-x[1], x[0])):
            if (i, j) not in used and j < len(t):
                return -1

            if s != prev_s:
                min_steps_i = 1
                break
            prev_s = s

        res.append((min_steps_i + cnt, i))

    print(min_steps)
    for step, pos in res:
        print(f"{step} {pos}")
