import heapq
import sys

def max_remaining_element(n, arr):
    # Convert the array into a min-heap
    heapq.heapify(arr)
    
    while len(arr) > 1:
        # Pop the two smallest elements
        smallest = heapq.heappop(arr)
        second_smallest = heapq.heappop(arr)
        
        # Compute the new value and push it back to the heap
        new_value = second_smallest - smallest
        heapq.heappush(arr, new_value)
    
    # The last remaining element
    return arr[0]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = max_remaining_element(n, arr)
    print(result)

