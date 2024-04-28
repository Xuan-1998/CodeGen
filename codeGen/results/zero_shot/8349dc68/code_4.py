import heapq
n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_heap = []
for i in range(0, n, k):
    window_sum = sum(arr[i:i+k])
    heapq.heappush(max_heap, -window_sum)
res = 0
while max_heap:
    res -= heapq.heappop(max_heap)
print(res)
