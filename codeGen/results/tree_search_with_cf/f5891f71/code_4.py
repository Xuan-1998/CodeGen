python
import sys

def max_remaining_element(n, arr):
    # Sort the array
    arr.sort()
    
    # Iterate and reduce
    for i in range(n - 1):
        arr[-1] -= arr[i]
    
    # The remaining element is the last element in the sorted array
    return arr[-1]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

