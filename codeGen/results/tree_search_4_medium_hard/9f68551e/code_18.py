import sys
import heapq

def solve():
    n = int(input())
    hp = list(map(int, input().split()))
    k = list(map(int, input().split()))

    dp = [[float('inf')] * (max(k) + 1) for _ in range(n + 1)]
    dp[0] = [0] * (max(k) + 1)

    pq = [(0, 0)]  # (mana, time)
    while pq:
        mana, t = heapq.heappop(pq)

        i = n
        j = t
        while i > 0 and j >= k[i-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-k[i-1]] + hp[i-1])
            i -= 1
            j -= k[i]

        if j == 0:
            return mana

        for x in range(1, min(j+1, max(k) + 1)):
            heapq.heappush(pq, (mana + x, j - x))

    return -1  # impossible to kill all monsters


print(solve())
