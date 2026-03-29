import heapq
import sys
input = sys.stdin.read

def max_remaining_element(n, array):
    # Convert array elements to negative to use Python's min-heap as a max-heap
    max_heap = [-x for x in array]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Extract two largest elements (in negative form, so smallest in negative form)
        largest = -heapq.heappop(max_heap)
        second_largest = -heapq.heappop(max_heap)
        
        # Compute the new value and push it back into the heap
        new_value = largest - second_largest
        heapq.heappush(max_heap, -new_value)
    
    # The last remaining element in the heap is the result
    return -max_heap[0]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:]))
    result = max_remaining_element(n, array)
    print(result)

