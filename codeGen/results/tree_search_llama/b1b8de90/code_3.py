def permute(n):
    memo = {}

    def recurse(x):
        if x in memo:
            return memo[x]
        
        # Base case: If x is 1, the permutation is already sorted
        if x == 1:
            return [i for i in range(1, n+1)]

        # Recursive case: Sort the first x-1 elements and then swap the x-th and (x-1)-th elements
        prev_perm = recurse(x-1)
        permuted_perm = prev_perm[:x-2] + [prev_perm[x-2], prev_perm[x-1]] + prev_perm[x:]
        memo[x] = permuted_perm
        return permuted_perm

    return ' '.join(map(str, recurse(n)))

# Example usage:
n = int(input())  # Read the input from stdin
print(permute(n))  # Print the resulting permutation to stdout
