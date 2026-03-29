def palindromic_partitions(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the diagonal to True, since single characters are palindromes
    for i in range(n + 1):
        dp[i][i] = True
    
    # Fill up the table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
    
    # Find all palindromic partitions
    partitions = []
    for partition_end in range(1, n + 1):
        if dp[0][partition_end]:
            partition = []
            i, j = 0, partition_end
            while i < j:
                if s[i] == s[j - 1]:
                    partition.append(s[i:j])
                    i = j
                else:
                    j -= 1
            partitions.append(partition)
    
    return partitions

# Read the input string from stdin
s = input()

# Print the result to stdout
print(palindromic_partitions(s))
