import sys
from collections import deque

def adjust_tree_values():
    # Read input
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))

    # Initialize DP table and queue
    dp = [[0] * 1000100 for _ in range(200010)]
    queue = deque([(0, 0)])  # (vertex, value)
    while queue:
        vertex, value = queue.popleft()
        if value < ranges[vertex-1][0]:
            dp[0][value] += 1
            queue.append((parent[vertex], value+1))
        elif value > ranges[vertex-1][1]:
            dp[0][value] += 1
            queue.append((parent[vertex], value-1))
        else:
            for child in range(vertex+1, n):
                if parent[child] == vertex:
                    queue.append((child, value))

    # Print the minimum number of operations needed
    print(sum(dp[0]))

adjust_tree_values()
