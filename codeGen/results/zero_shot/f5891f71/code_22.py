def max_remaining_element(n, arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize the result with the first element
    result = arr[0]
    
    # Subtract each of the remaining elements
    for i in range(1, n):
        result -= arr[i]
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    print(max_remaining_element(n, arr))

