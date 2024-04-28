import queue
from functools import reduce

def merge_arrays(*arrays):
    # Get the length of the longest array
    max_len = max(len(arr) for arr in arrays)
    
    # Initialize the result queue with nils
    result = queue.Queue()
    for _ in range(max_len):
        result.put(None)

    # Iterate through each input array and append its elements to the result queue
    for arr in arrays:
        for elem in arr:
            while result.get() is not None:  # Consume any existing nils
                pass
            result.put(elem)
    
    # Convert the queue to a list
    return list(result.queue)

# Test your function
if __name__ == "__main__":
    n = int(input())
    arrays = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        arrays.append(arr)
    print(merge_arrays(*arrays))
