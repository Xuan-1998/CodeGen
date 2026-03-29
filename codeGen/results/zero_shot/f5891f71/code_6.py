def max_remaining_element(n, arr):
    # Calculate the sum of absolute values of all elements
    max_value = sum(abs(x) for x in arr)
    return max_value

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = max_remaining_element(n, arr)
    print(result)

