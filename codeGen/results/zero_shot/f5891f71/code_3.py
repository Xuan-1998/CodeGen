def maximize_remaining_element(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the remaining element as the smallest element
    remaining_element = arr[0]
    
    # Iterate over the rest of the elements and perform the subtraction
    for i in range(1, n):
        remaining_element = remaining_element - arr[i]
    
    return remaining_element

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = maximize_remaining_element(n, arr)
    print(result)

