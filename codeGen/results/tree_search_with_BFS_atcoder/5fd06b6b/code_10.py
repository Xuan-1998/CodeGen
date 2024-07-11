import heapq

n = int(input().strip())
counts = list(map(int, input().strip().split()))

heap = []
sum_counts = 0

for count in counts:
    heapq.heappush(heap, -count)
    while heap and -heap[0] > count:
        sum_counts += -heapq.heappop(heap)
    sum_counts += count

print(sum_counts)

