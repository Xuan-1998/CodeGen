python
import sys

def max_remaining_element(n, arr):
    # If there's only one element, return it
    if n == 1:
        return arr[0]

    # Sort the array to ensure we always subtract the smallest possible adjacent element
    arr.sort()

    # Perform the operations greedily
    for i in range(n - 1):
        arr[i + 1] = arr[i + 1] - arr[i]

    # The last element will be the maximum possible remaining element
    return arr[-1]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

