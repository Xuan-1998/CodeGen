def max_beauty(n, bad_primes):
    # Initialize a list to store the maximum beauty values for all subarrays
    max_beauty = [0] * (n + 1)
    
    # Initialize a dictionary to memoize the results of subproblems
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base case: empty subarray or single-element subarray
        if i > j:
            max_beauty[i] = 0
        elif i == j:
            max_beauty[i] = 1 if array[i] not in bad_primes else 0
        
        # Recursive case: combine the beauty values of non-overlapping subarrays
        else:
            good_prime = array[i] not in bad_primes
            exclude = dfs(i, j - 1)
            include = 0 if good_prime else 1
            max_beauty[i] = max(exclude, include)
        
        memo[(i, j)] = max_beauty[i]
        return max_beauty[i]
    
    # Main function to compute the maximum beauty value for the entire array
    max_beauty[0] = dfs(0, n - 1)
    print(max_beauty[0])

