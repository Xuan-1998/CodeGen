def max_remaining_element(n, arr):
    # Sort the array based on absolute values in descending order
    arr.sort(key=abs, reverse=True)

    # Initialize the remaining element with the first element
    remaining = arr[0]

    # Iterate through the rest of the array
    for i in range(1, n):
        remaining -= arr[i]

    return remaining

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

