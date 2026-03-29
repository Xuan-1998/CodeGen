import sys
from collections import deque

# Read input from stdin
t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Initialize queue for BFS
    queue = deque([(0, 0, 0)])  # (index, x_sum, y_sum)

    min_F = float('inf')
    while queue:
        i, x_sum, y_sum = queue.popleft()
        
        if i == n: 
            F = a[0] * x_sum + y_sum * a[-1]
            min_F = min(min_F, F)
        else:
            for j in range(a[i], 2*10**5+1):
                if (x_sum - s) * (j - s) >= 0 and (y_sum - s) * (a[i] - j) >= 0:
                    queue.append((i + 1, x_sum + j, y_sum + a[i] - j))
    print(min_F)
