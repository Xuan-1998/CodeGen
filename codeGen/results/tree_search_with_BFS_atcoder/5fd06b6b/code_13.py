import heapq

n = int(input().strip())
counts = list(map(int, input().strip().split()))

heap = []
sum_counts = 0

for i in range(n):
    heapq.heappush(heap, -counts[i])
    if len(heap) > i + 1:
        sum_counts -= heapq.heappop(heap)

print(sum_counts)

