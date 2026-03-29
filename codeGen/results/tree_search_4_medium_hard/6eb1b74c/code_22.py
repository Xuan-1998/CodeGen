import sys
from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    strings = [input() for _ in range(n)]

    dp = [[[float('inf')] for _ in range(2)] for _ in range(len(t) + 1)]
    dp[0][0][0] = 0

    seen_strings = defaultdict(int)

    for i in range(1, len(t) + 1):
        for j in range(min(i, n), -1, -1):
            if strings[j] in t[i-1:]:
                k = 1
            else:
                k = 0

            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][seen_strings.get(strings[j])] + 1)
            seen_strings[strings[j]] = k
        if all(seen_strings[s] for s in strings):
            break

    if dp[-1][-1][0] == float('inf'):
        print(-1)
    else:
        m = dp[-1][-1][0]
        used_strings = []
        i, j = len(t), n-1
        while m > 0 and j >= 0:
            if strings[j] in t[i-1:]:
                used_strings.append((j, i))
                i -= len(strings[j])
                k = 1
            else:
                k = 0
            m -= 1
            j -= 1

        for pair in used_strings:
            print(*pair)
