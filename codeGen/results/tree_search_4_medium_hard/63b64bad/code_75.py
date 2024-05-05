import sys
from collections import deque

def get_final_y(n, sequence):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if x <= 0 or x > n:
            return -1
        dp[x][y] = y

        a_x = sequence[x]
        new_x = x + a_x
        new_y = y + a_x
        queue.append((new_x, new_y))

    return dp[n][0]

n = int(input())
sequence = list(map(int, input().split()))
print(get_final_y(n, sequence))
