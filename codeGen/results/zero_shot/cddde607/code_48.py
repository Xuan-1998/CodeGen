from collections import deque

def numPaths(K, N, arr):
    dirr = [(0, 1), (1, 0)]
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    res = 0
    while queue:
        i, j, count = queue.popleft()
        if i == N - 1 and j == N - 1 and count == K:
            res += 1
        for dx, dy in dirr:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and arr[ni][nj] != 0:
                queue.append((ni, nj, count + arr[ni][nj]))
                visited.add((ni, nj))
    return res
