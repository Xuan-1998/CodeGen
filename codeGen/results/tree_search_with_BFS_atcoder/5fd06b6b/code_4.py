import heapq

n = int(input())
seq = list(map(int, input().split()))

heap = []
sum_ = 0

for i in range(n - 1, -1, -1):
    heapq.heappush(heap, -seq[i])
    sum_ -= heapq.heappop(heap)

print(-sum_)

