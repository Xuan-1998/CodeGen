def merge_ways(M, i=0):
    if i >= len(M):
        return 1  # Base case: all arrays merged
    ways = 0
    for j in range(len(M[i])):
        new_V = V + [M[i][j]]
        ways += merge_ways(new_V, i+1)
    return ways % (10**9 + 7)

n = int(input())  # Read the size of the input array
M = list(map(int, input().split()))  # Read the input array

V = []  # Initialize the collection V
result = merge_ways(M)
print(result)  # Print the result
