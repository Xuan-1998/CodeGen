import heapq

def mergeable_permutation(n, p):
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    pq = []
    for i in range(2 * n):
        while pq and pq[0][0] <= i - n:
            heapq.heappop(pq)
        if pq and p[i] < p[pq[0][0]]:
            dp[i // 2][i % 2].append((p[i], i))
        else:
            heapq.heappush(pq, (p[i], i))

    for i in range(n):
        for j in range(i + 1, n):
            if any(a > p[2 * k] and b < p[2 * k] for a, k in dp[i // 2][i % 2] for b in dp[j // 2][j % 2]):
                return "YES"
    return "NO"

n = int(input())
p = list(map(int, input().split()))
print(mergeable_permutation(n, p))
