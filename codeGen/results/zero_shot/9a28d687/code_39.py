import sys
from collections import deque

def min_cost_to_sort_strings():
    n = int(sys.stdin.readline().strip())
    costs = list(map(int, sys.stdin.readline().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    # Initialize a 2D array to store the minimum cost
    dp = [[0] * (n + 1) for _ in range(100000 + 1)]

    # Initialize a queue to perform BFS
    queue = deque([(0, ""))])

    while queue:
        i, s = queue.popleft()
        if i == n:
            return dp[i][i]
        for j in range(i + 1):
            cost_to_reverse = costs[j] * len(s[:j])
            new_string = s[:j][::-1] + s[j:]
            dp[i][n] = min(dp[i][n], dp[i - j - 1][j] + cost_to_reverse)
            queue.append((i - j, new_string))

    return -1

print(min_cost_to_sort_strings())
