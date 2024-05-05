import itertools

def num_ways(M):
    n = len(M)
    perms = list(itertools.permutations(M))
    ways = 0
    for perm in perms:
        sorted_perm = sorted(perm)
        if sorted_perm == M:
            ways += 1
    return ways % (10**9 + 7)

# Example usage:
n = int(input())  # Read the size of array M from input
M = [int(x) for x in input().split()]  # Read the elements of M from input
print(num_ways(M))  # Print the result
