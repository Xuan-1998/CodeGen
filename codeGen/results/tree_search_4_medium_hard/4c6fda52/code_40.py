from collections import deque

def solve():
    n, k = map(int, input().split())
    s = list(input())

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()
        if i >= n or j >= k:
            continue
        if s[i] != 'RGB'[i % 3]:
            dp[i][j] += 1

        for x in range(3):
            if s[i] == 'RGB'[x]:
                break
        next_i = i + 1
        for x in range(3):
            if s[next_i] == 'RGB'[x]:
                break
        next_i += 1

        for j2 in range(j, min(k, next_i)):
            dp[i][j2] = min(dp[i-1][j2], dp[i-1][max(0, j2-1)], 1 + dp[i-1][min(j2-1, k-1)])

        q.append((next_i, j))

    return sum(min(dp[i][k-1], i) for i in range(n - k+2))
