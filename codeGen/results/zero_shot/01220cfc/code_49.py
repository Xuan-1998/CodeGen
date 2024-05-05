from collections import deque

def canReach(arr):
    n = len(arr)
    visited = [False] * n

    def bfs(i):
        if i == n - 1:
            return True
        visited[i] = True
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for j in range(1, arr[node] + 1):
                next_node = node + j
                if next_node >= n or visited[next_node]:
                    continue
                if bfs(next_node):
                    return True
        return False

    return bfs(0)

# Read input from standard input
arr = [int(x) for x in input().split()]

print(canReach(arr))
