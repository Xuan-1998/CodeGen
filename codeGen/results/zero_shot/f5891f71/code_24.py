import heapq
import sys

def max_remaining_element(n, array):
    if n == 1:
        return array[0]
    
    # Convert array to a min-heap
    heapq.heapify(array)
    
    while len(array) > 1:
        # Get the smallest element
        smallest = heapq.heappop(array)
        # Get the next smallest element
        next_smallest = heapq.heappop(array)
        
        # Update the smallest element
        new_value = smallest - next_smallest
        
        # Push the updated value back into the heap
        heapq.heappush(array, new_value)
    
    # The remaining element in the heap is the answer
    return array[0]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:]))
    result = max_remaining_element(n, array)
    print(result)

