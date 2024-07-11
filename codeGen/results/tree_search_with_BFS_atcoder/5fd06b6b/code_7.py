import heapq

n = int(input().strip())
sequence = list(map(int, input().strip().split()))

queue = []
total = 0
for i in range(n):
    heapq.heappush(queue, -sequence[i])
    total -= heapq.heappop(queue)

print(total)

