import heapq

n = int(input().strip())
counts = list(map(int, input().strip().split()))
heapq.heapify(counts)
result = 0

for i in range(n):
    min_count = heapq.heappop(counts)
    result += min_count

print(result)

