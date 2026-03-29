import heapq
import sys
input = sys.stdin.read

def maximize_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    # Create a min-heap with the negative values to simulate a max-heap
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        # Get the two largest elements (most negative in the heap)
        largest = -heapq.heappop(max_heap)
        second_largest = -heapq.heappop(max_heap)
        
        # Subtract second largest from largest
        new_value = largest - second_largest
        
        # Push the result back into the heap
        heapq.heappush(max_heap, -new_value)
    
    # The remaining element in the heap is the result
    return -max_heap[0]

def main():
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    print(maximize_remaining_element(n, arr))

if __name__ == "__main__":
    main()

