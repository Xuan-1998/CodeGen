import sys
from collections import deque

n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip()))
dp = [0] * (n - 1)

queue = deque([(0, 0)])  # (index, or_value)
while queue:
    i, or_val = queue.popleft()
    if i < n - 1:  # If not at the end
        for j in range(i + 1, n):
            new_or_val = or_val | s[j]
            dp[j - 1] = max(dp[j - 1], new_or_val)
            queue.append((j, new_or_val))

print(bin(max(dp))[2:].zfill(n))  # Print the answer
