def memoized_palindromic_partitions(s):
    memo = {}
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return [[s[i:j+1]]]
        
        partitions = []
        for k in range(i + 1, j + 1):
            left = s[i:k]
            right = s[k-1:i:-1]  # Reverse the right part
            if left == right:  # Check if it's a palindrome
                for p in helper(i, k - 2):  # Recurse on the left and right parts
                    for q in helper(k, j):
                        partitions.append([left] + p + [right] + q)
        memo[(i, j)] = partitions
        return partitions
    
    return helper(0, len(s) - 1)
