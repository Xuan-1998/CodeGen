from collections import deque

def count_paths_to_collect_k_coins(k, n, arr):
    directions = [(0, 1), (1, 0)]
    visited = [[[False for _ in range(200+1)] for _ in range(n+1)] for _ in range(n+1)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = True

    while queue:
        i, j, total_coins = queue.popleft()

        if i == n - 1 and j == n - 1:
            return total_coins

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj][total_coins + arr[ni][nj]]:
                queue.append((ni, nj, total_coins + arr[ni][nj]))
                visited[ni][nj][total_coins + arr[ni][nj]] = True

    return 0
