def partition_palindromes(s):
    n = len(s)
    
    # Create a 2D array dp[][] where dp[i][j] is true if the substring from index i to j is a palindrome.
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    # Fill up the dp[] array in a bottom-up manner, starting from single characters and gradually constructing longer palindromic partitions.
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
    
    # Initialize the result with an empty partition.
    partitions = [[]]
    
    # Iterate over all possible lengths of palindromic partitions.
    for length in range(2, n+1):
        new_partitions = []
        for i in range(n-length+1):
            j = i + length - 1
            if dp[i][j]:
                # If the substring from index i to j is a palindrome,
                # then consider it as part of a larger palindrome.
                for partition in partitions:
                    new_partition = partition + [s[i:j+1]]
                    new_partitions.append(new_partition)
        partitions = new_partitions
    
    return partitions

# Example usage
s = input()
partitions = partition_palindromes(s)

# Print the result
for i, partition in enumerate(partitions):
    print(f"Partition {i+1}: {' '.join(partition)}")
