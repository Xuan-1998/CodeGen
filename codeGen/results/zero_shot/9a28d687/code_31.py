import heapq

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

pq = [(0, 0, s) for s in strings]
heapq.heapify(pq)
sorted_strings = []
total_cost = 0
while pq:
    _, cost, string = heapq.heappop(pq)
    total_cost += cost
    while sorted_strings and string > sorted_strings[-1]:
        total_cost -= cost
        string = string[::-1]
    sorted_strings.append(string)

print(total_cost if len(sorted_strings) == n else -1)
