import re
from collections import deque

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    dp = [[False] * (len(t) + 1) for _ in range(len(t) + 1)]
    visited = set()

    queue = deque([(0, 0)])
    dp[0][0] = True

    steps = 0
    while queue:
        pos, step = queue.popleft()
        if dp[step][pos]:
            continue

        for i in range(1, len(t) + 1):
            if pos + i > len(t):
                break

            substring = t[pos:pos + i]
            for s in strings:
                if re.match(s, substring):
                    queue.append((i, step + 1))
                    dp[step + 1][pos] = True
                    visited.add((s, pos))

    if not visited:
        print(-1)
    else:
        print(len(visited) - 1)

        for i in range(len(t)):
            for j in range(i, len(t)):
                if (t[i:j], i) in visited:
                    print(f"{i} {j}")
