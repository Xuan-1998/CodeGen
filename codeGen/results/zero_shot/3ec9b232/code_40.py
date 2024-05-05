# Read the input
n = int(input())
M = list(map(int, input().split()))

# Initialize an empty set to store unique permutations
permutations = set()

# Define a recursive function to generate all possible permutations of M
def permute(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        remaining = arr[:i] + arr[i+1:]
        for p in permute(remaining):
            result.append([arr[i]] + p)
    return result

# Generate all possible permutations of M
for p in permute(M):
    # Check if the permutation can be sorted to match M
    if sorted(p) == M:
        # Add the permutation to the set
        permutations.add(tuple(p))

# Calculate the number of unique permutations
unique_permutations = len(permutations)

# Print the result
print(unique_permutations % (10**9 + 7))
