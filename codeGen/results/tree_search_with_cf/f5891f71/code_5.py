python
import heapq
import sys

input = sys.stdin.read
def main():
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    if n == 1:
        print(arr[0])
        return

    # Use a max heap to always get the largest element efficiently
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        largest = -heapq.heappop(max_heap)
        second_largest = -heapq.heappop(max_heap)
        new_value = largest - second_largest
        heapq.heappush(max_heap, -new_value)

    print(-max_heap[0])

if __name__ == "__main__":
    main()

