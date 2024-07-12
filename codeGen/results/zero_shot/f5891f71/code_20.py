def max_remaining_value(n, arr):
    # Sort the array to facilitate the greedy approach
    arr.sort()
    
    # Initialize the result with the first element
    result = arr[0]
    
    # Iterate over the rest of the array and apply the operation
    for i in range(1, n):
        result = abs(result - arr[i])
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    print(max_remaining_value(n, arr))

