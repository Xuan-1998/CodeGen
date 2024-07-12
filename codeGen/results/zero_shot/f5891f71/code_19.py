def max_remaining_element(n, arr):
    # Sort the array to ensure we can perform operations optimally
    arr.sort()
    
    # Initialize the remaining element as the first element
    remaining = arr[0]
    
    # Perform operations by subtracting the smallest remaining element each time
    for i in range(1, n):
        remaining = remaining - arr[i]
    
    return remaining

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

