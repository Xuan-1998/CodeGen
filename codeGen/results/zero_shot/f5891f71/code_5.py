python
import heapq
import sys

def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]

    # Convert all elements to negative to use min-heap as max-heap
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        largest = -heapq.heappop(max_heap)
        second_largest = -heapq.heappop(max_heap)
        new_value = largest - second_largest
        heapq.heappush(max_heap, -new_value)

    return -max_heap[0]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    result = max_remaining_element(n, arr)
    print(result)

