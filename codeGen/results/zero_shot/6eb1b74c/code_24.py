import sys
from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    dp = [[-1] * (len(t) + 1) for _ in range(len(t) + 1)]
    dp[0][0] = 0

    used_strings = set()

    min_steps = float('inf')
    steps = []

    for i in range(1, len(t) + 1):
        for j in range(i + 1):
            if t[j:i] in strings:
                if dp[i-1][j]:
                    new_step = dp[i-1][j]
                else:
                    new_step = 0
                used_strings.add(t[j:i])
                dp[i][j] = new_step + 1
                min_steps = min(min_steps, dp[i][j])
            elif i > j and dp[i-j][j]:
                dp[i][j] = dp[i-j][j] + 1
                if dp[i][j] == min_steps:
                    steps.append((used_strings.pop(), j))
            else:
                dp[i][j] = -1

    print(min_steps)
    for step in steps:
        print(*step)

if __name__ == "__main__":
    solve()
