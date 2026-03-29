def max_remaining_element(n, array):
    if n == 1:
        return array[0]
    
    current_max = array[0]
    
    for i in range(1, n):
        current_max = max(current_max - array[i], array[i] - current_max)
    
    return current_max

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    array = list(map(int, data[1:]))
    
    print(max_remaining_element(n, array))

