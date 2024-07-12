def max_remaining_element(n, array):
    # Start from the end of the array and work backwards
    for i in range(n - 1, 0, -1):
        array[i - 1] = array[i - 1] - array[i]
    
    # The first element will be the remaining element
    return array[0]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    array = list(map(int, data[1:n+1]))
    
    result = max_remaining_element(n, array)
    print(result)

