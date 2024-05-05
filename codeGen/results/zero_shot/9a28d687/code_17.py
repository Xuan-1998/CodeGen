import heapq

# Read the input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Create a priority queue with the strings and their costs
pq = [(0, strings[0])]
min_cost = 0

for i in range(1, n):
    if pq[0][0] == costs[i]:
        # If the cost of reversing the current string matches the top cost, pop it from the queue
        heapq.heappop(pq)
    # Add the new string and its cost to the priority queue
    heapq.heappush(pq, (costs[i], strings[i]))

# Sort the strings in lexicographical order using the priority queue
sorted_strings = []
while pq:
    _, curr_string = heapq.heappop(pq)
    sorted_strings.append(curr_string)

# Calculate and print the minimum total cost required to sort the strings in lexicographical order
min_cost = sum(costs[i] for i, _ in enumerate(sorted_strings))
print(min_cost if min_cost == costs[0] else -1)
