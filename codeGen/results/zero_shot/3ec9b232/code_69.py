def count_valid_permutations(permutations):
    return len(filter_out_invalid_permutations(permutations))

# Test the code
n = int(input())  # Read n from stdin
M = list(map(int, input().split()))  # Read M from stdin

permutations = generate_permutations(M)
valid_permutations = filter_out_invalid_permutations(permutations)
count = count_valid_permutations(valid_permutations)

print(count % (10**9 + 7))  # Print the result to stdout
