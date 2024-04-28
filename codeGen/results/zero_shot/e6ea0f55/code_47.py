import heapq
n, k = map(int, input().split())
nums = list(map(int, input().split()))
pq = [(0, 0)]
ans = 0
seen = set()
while pq:
    s, i = heapq.heappop(pq)
    if i+k+1 > n or (i, s) in seen:
        continue
    ans = max(ans, s)
    for j in range(i+k+1, min(n, i+2*k)+1):
        heapq.heappush(pq, (s+nums[j], j))
    seen.add((i, s))
print(ans)
