def max_remaining_element(n, arr):
    # Start with the first element
    current_value = arr[0]
    
    # Iterate through the array from the second element to the end
    for i in range(1, n):
        current_value = current_value - arr[i]
    
    return current_value

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

