import heapq

n = int(input())  # number of strings
costs = list(map(int, input().split()))  # costs for each string
strings = [input() for _ in range(n)]  # given strings

# Create a priority queue to store the strings based on their lexicographical order
pq = []
for i in range(n):
    heapq.heappush(pq, (0, strings[i]))

min_cost = 0
prev_string = ''
while pq:
    _, curr_string = heapq.heappop(pq)
    if curr_string < prev_string:  # check if the current string is smaller than the previous one
        min_cost += costs[0]  # increment the cost by the cost of reversing the first string
    else:
        min_cost += costs[n - 1]  # increment the cost by the cost of reversing the last string
    prev_string = curr_string

print(min_cost) if pq else print(-1)
