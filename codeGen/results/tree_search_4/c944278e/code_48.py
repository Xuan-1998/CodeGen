from collections import deque

n = int(input())
s = input()

dp = [[False] * (1 << n) for _ in range(n + 1)]

for i in range(n + 1):
    for mask in range(1 << n):
        if s[i - 1] == '1':
            dp[i][mask | (1 << (n - i))] = True
        else:
            dp[i][mask] = False

result = set()
queue = deque([(0, 0)])

while queue:
    phase, mask = queue.popleft()
    if phase > n:
        continue
    for i in range(n):
        if not (mask & (1 << i)):
            new_mask = mask | (1 << i)
            new_phase = phase + 1
            if dp[new_phase][new_mask]:
                result.add(new_mask)

print('\n'.join(map(str, sorted(list(result)))).split())
