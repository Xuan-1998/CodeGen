import sys
from collections import deque

def solution():
    n = int(input())
    w = list(map(int, input().split()))
    e = [list(map(int, input().split())) for _ in range(n-1)]

    dp = [[0]*n for _ in range(n)]
    parent = [-1]*n
    queue = deque([0])

    while queue:
        i = queue.popleft()
        for j, c in enumerate(e[i-1]):
            e[j][1] -= 1
            if not e[j][1]:
                parent[e[j][2]] = i
                queue.append(e[j][2])
            if e[j][0] == n-1:
                return min(w[i], w[i-1] + c)

    return -1

print(solution())
