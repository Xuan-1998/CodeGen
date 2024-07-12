python
import heapq
import sys

def maximum_remaining_element(n, arr):
    # Convert the array into a max-heap (using negative values for max-heap simulation)
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Extract the two largest elements
        largest = -heapq.heappop(max_heap)
        second_largest = -heapq.heappop(max_heap)
        
        # Perform the operation (largest - second_largest)
        new_value = largest - second_largest
        
        # Push the result back into the heap (if it's not zero)
        if new_value != 0:
            heapq.heappush(max_heap, -new_value)
    
    # The last remaining element in the heap
    return -max_heap[0]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = maximum_remaining_element(n, arr)
    print(result)

