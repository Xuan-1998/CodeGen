import sys
from collections import deque

n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [[False] * (k + 1) for _ in range(n + 1)]

for i in range(k + 1):
    dp[0][i] = True

q = deque([(0, 0)])
while q:
    pos, last_jump_len = q.popleft()
    for jump_len in range(1, k + 1):
        next_pos = pos + (jump_len - 1) // 3 * jump_len
        if next_pos < len(stones) and dp[next_pos][jump_len % 3]:
            dp[next_pos][jump_len % 3] = False
            q.append((next_pos, jump_len))
        else:
            break

print("YES" if any(dp[-1]) else "NO")
