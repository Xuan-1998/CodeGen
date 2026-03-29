import heapq

n = int(input().strip())
counts = list(map(int, input().strip().split()))

pq = []
total_sum = 0

for i in range(n):
    heapq.heappush(pq, counts[i])

for i in range(n):
    min_count = heapq.heappop(pq)
    total_sum += min_count

print(total_sum)

