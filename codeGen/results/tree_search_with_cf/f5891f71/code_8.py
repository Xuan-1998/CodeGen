python
def max_possible_value(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the result with the largest element
    result = arr[-1]
    
    # Iterate from the second smallest to the second largest element
    for i in range(n - 1):
        result -= arr[i]
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    print(max_possible_value(n, arr))

