import heapq
import sys
input = sys.stdin.read

def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    # Convert array to a max-heap
    arr = [-x for x in arr]
    heapq.heapify(arr)
    
    while len(arr) > 1:
        # Extract the largest element
        largest = -heapq.heappop(arr)
        # Extract the next largest element
        next_largest = -heapq.heappop(arr)
        
        # Perform the operation: largest - next_largest
        new_value = largest - next_largest
        
        # Push the result back into the heap
        heapq.heappush(arr, -new_value)
    
    # The last remaining element in the heap is the answer
    return -arr[0]

# Read input
data = input().split()
n = int(data[0])
arr = list(map(int, data[1:]))

# Get the result
result = max_remaining_element(n, arr)

# Print the result
print(result)

