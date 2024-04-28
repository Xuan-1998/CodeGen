import heapq
n = int(input())
a = list(map(int, input().split()))
heap = []
max_points = 0
for i in range(n):
    while heap and heap[0] < a[i]:
        heapq.heappop(heap)
    if heap:
        max_points += len(heap)
    heapq.heappend(heap, a[i])
print(max_points)
