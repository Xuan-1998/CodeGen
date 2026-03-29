from collections import deque

def minF(a, s):
    n = len(a)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    queue = deque([(0, 0)])

    while queue:
        i, f = queue.popleft()
        for j in range(i+1, n+1):
            f += a[j-1]
            for x in range(s+1, max(a[j-1], s) + 1):
                y = a[j-1] - x
                if (x-s)*(y-s) >= 0:
                    dp[j] = min(dp[j], f + x*y)

        queue.extend([(i+1, f+a[i])] for i in range(n))

    return dp[-1]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(minF(a, s))
