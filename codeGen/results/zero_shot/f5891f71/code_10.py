def max_remaining_element(n, arr):
    # Compute the sum of absolute values of all elements
    total_sum = sum(abs(x) for x in arr)
    
    # Print the result
    print(total_sum)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    max_remaining_element(n, arr)

