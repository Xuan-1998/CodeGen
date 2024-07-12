python
def max_remaining_element(n, arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Perform the operations
    remaining_value = arr[0]
    for i in range(1, n):
        remaining_value -= arr[i]
    
    return remaining_value

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

