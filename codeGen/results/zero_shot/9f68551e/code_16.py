import sys
from collections import deque

def min_mana_required(n, k, h):
    k = list(map(int, k.split()))
    h = list(map(int, h.split()))
    dp = [0] * (max(k) + 1)
    q = deque([(h[0], 0)])
    for i in range(1, n):
        while q and q[0][0] <= k[i]:
            mana, _ = q.popleft()
            dp[k[i]] = max(dp[k[i]], mana + (k[i] - h[i]))
            if i < n - 1:
                q.append((h[i], k[i]))
    return min(dp)

t = int(input())
for _ in range(t):
    n = int(input())
    k = input()
    h = input()
    print(min_mana_required(n, k, h))
