import heapq

n = int(input().strip())
counts = list(map(int, input().strip().split()))
counts.reverse()

pq = []
sum = 0

for c in counts:
    if pq and -pq[0] > c:
        sum += -heapq.heappop(pq)
    heapq.heappush(pq, -c)

while pq:
    sum += -heapq.heappop(pq)

print(sum)

