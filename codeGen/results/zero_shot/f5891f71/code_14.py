import heapq
import sys

def maximize_remaining_element(n, arr):
    # Convert the array into a min-heap based on absolute values
    heap = [(abs(x), x) for x in arr]
    heapq.heapify(heap)
    
    # Perform the operations until only one element remains
    while len(heap) > 1:
        # Pop the smallest two elements based on absolute value
        _, x = heapq.heappop(heap)
        _, y = heapq.heappop(heap)
        
        # Calculate the new value of x after the operation
        new_x = x - y
        
        # Push the new value back into the heap
        heapq.heappush(heap, (abs(new_x), new_x))
    
    # The remaining element is the result
    return heap[0][1]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = maximize_remaining_element(n, arr)
    print(result)

