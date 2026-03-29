import heapq

n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Pair each element with its index (1-indexed), then sort in ascending order of value and descending order of index
sequence = sorted(((v, i+1) for i, v in enumerate(sequence)), reverse=True)

# Initialize a priority queue (heap) and a variable to keep track of the sum
heap = []
sum = 0

# Iterate through the sorted sequence
for v, i in sequence:
    # If the heap is empty or the top of the heap is less than the current day, push the current day into the heap
    if not heap or heap[0] > i:
        heapq.heappush(heap, i)
    # Otherwise, pop the top of the heap, add it to the sum, and push the current day into the heap
    else:
        sum += heapq.heappop(heap)
        heapq.heappush(heap, i)

# After iterating through the sequence, while the heap is not empty, pop the top of the heap and add it to the sum
while heap:
    sum += heapq.heappop(heap)

# Print the sum
print(sum)

