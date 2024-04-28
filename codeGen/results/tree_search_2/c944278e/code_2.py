def find_winning_teams(n):
    # Base case: return an empty list when n = 0
    if n == 0:
        return []

    # Initialize a dictionary to store memoized results
    memo = {0: []}

    def recursive_helper(i, subset):
        # If we've already computed this result, return the cached value
        if (i, tuple(sorted(subset))) in memo:
            return memo[(i, tuple(sorted(subset)))]
        
        # Compute the result for this phase and update the memo dictionary
        if s[i - 1] == '1':
            winning_subset = subset | {2 ** i - 1}
        else:
            winning_subset = set()

        result = list(recursive_helper(i - 1, winning_subset))
        if result:
            result.append(2 ** i - 1)
        memo[(i, tuple(sorted(subset)))] = sorted(list(set(result)))
        return result

    # Call the recursive helper function and return the result
    return recursive_helper(n, set())

# Read input from stdin
n = int(input())
s = input().strip()

# Call the find_winning_teams function and print the results to stdout
print(*find_winning_teams(n), sep='\n')
