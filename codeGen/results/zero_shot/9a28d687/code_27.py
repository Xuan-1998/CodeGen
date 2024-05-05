import heapq

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

heap = []
for i in range(n):
    if strings[i][::-1] < strings[i]:
        cost = costs[i]
    else:
        cost = 0
    heapq.heappush(heap, (-cost, strings[i]))

result = []
while heap:
    string = heapq.heappop(heap)[1]
    result.append(string)

print(-sum(costs) if len(result) == n else -1)
