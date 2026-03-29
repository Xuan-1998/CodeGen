import heapq

# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Initialize priority queue with departments
pq = [(0, i) for i in range(1, m+1)]
heapq.heapify(pq)

# Initialize state and result variables
seen = False
prob = 0

# Greedily add players until the team is complete
while pq and prob < n:
    count, department = heapq.heappop(pq)
    if department == h:
        seen = True
    prob += count
    # If we have added at least one player from the department of interest, 
    # we can stop adding players as the probability is guaranteed to be 1.
    if seen:
        break

# Calculate and print the result
if prob < n:
    prob = -1
print(prob)
