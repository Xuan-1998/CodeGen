import heapq

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

heap = [(0, 0)]  # (cost, reversed_count)
min_total_cost = float('inf')

for i in range(len(strings)):
    if not heap or heap[0][1] > costs[i]:
        heapq.heappush(heap, (costs[i], 0))

    while heap:
        cost, reversed_count = heapq.heappop(heap)

        for j in range(i):
            if strings[j] < strings[i]:
                new_cost = cost + costs[i]
                if new_cost <= min_total_cost and new_cost >= 0:
                    min_total_cost = new_cost
                    break
                else:
                    return -1

        if heap and heap[0][1] > reversed_count:
            heapq.heappush(heap, (cost + costs[i], reversed_count + 1))
        elif not heap or heap[0][1] <= reversed_count:
            continue

print(min_total_cost)
