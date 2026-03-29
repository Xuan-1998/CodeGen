def merge_ways(M):
    n = len(M)
    # Sort M
    sorted_M = sorted(M)
    
    # Initialize the result as 1 (the empty collection)
    ways = 1
    
    for i in range(1, n):
        if sorted_M[i-1] != sorted_M[i]:
            # We need to add a new element to V
            ways *= i
            ways %= 10**9 + 7
    
    return ways

# Read the input from stdin
n = int(input())
M = list(map(int, input().split()))

# Call the function and print the result to stdout
print(merge_ways(M))
