import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        ranges.append((l, r))

    dp = [[0] * n for _ in range(n)]
    queue = deque([(n - 1, n - 1)])
    while queue:
        i, j = queue.popleft()
        if i == j:
            continue
        for k in range(i + 1, j):
            if parent[k] != i:
                continue
            diff = ranges[k][1] - ranges[k][0]
            dp[i][j] += dp[i][k] + (diff if k > i else 0)
        queue.extend([(i, k) for k in range(i - 1, j)])


    print(dp[0][n - 2])

if __name__ == "__main__":
    solve()
