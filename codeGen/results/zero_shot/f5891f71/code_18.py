def max_remaining_element(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the remaining element with the first element of the sorted array
    remaining_element = arr[0]
    
    # Perform the operations from left to right
    for i in range(1, n):
        remaining_element = remaining_element - arr[i]
    
    return remaining_element

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = max_remaining_element(n, arr)
    print(result)

