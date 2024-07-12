python
import heapq
import sys

input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:n+1]))

    if n == 1:
        print(array[0])
        return

    # Use a min-heap to manage the elements
    heapq.heapify(array)

    while len(array) > 1:
        # Extract the two smallest elements
        x = heapq.heappop(array)
        y = heapq.heappop(array)

        # Perform the operation and push the result back
        new_value = x - y
        heapq.heappush(array, new_value)

    # The last remaining element is our result
    print(array[0])

if __name__ == "__main__":
    main()

