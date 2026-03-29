import heapq

# Read the length of the sequence
n = int(input().strip())

# Read the sequence
sequence = list(map(int, input().strip().split()))

# Initialize an empty priority queue (heap) and a variable `sum` to keep track of the minimum possible sum
heap = []
total = 0

# Iterate over the sequence from the first day to the 'n'th day
for i in range(n):
    # Push the count of elements strictly greater than the current element in the sequence on the 'i'th day (mi) into the priority queue
    # Multiply by -1 to simulate a max-heap
    heapq.heappush(heap, -sequence[i])

    # If the size of the priority queue is greater than the count of elements strictly greater than the current element in the sequence on the next day (mi+1), then remove the largest element from the priority queue and add it to the `sum`
    if i < n - 1 and len(heap) > sequence[i + 1]:
        total += -heapq.heappop(heap)

# Finally, while the priority queue is not empty, remove the largest element from the priority queue and add it to the `sum`
while heap:
    total += -heapq.heappop(heap)

# Print the value of `sum` as the minimum possible sum of the counts of elements strictly less than the current element in the sequence over 'n' days
print(total)

