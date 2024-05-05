def partition_palindromes(s, partition=[], palindromic_partitions=[]):
    if not s:
        return palindromic_partitions + [partition]
    else:
        for i in range(1, len(s) + 1):
            part = s[:i]
            if part == part[::-1]:  # Check if the partition is palindromic
                new_partition = partition + [part]
                palindromic_partitions.extend(partition_palindromes(s[i:], new_partition, palindromic_partitions))
    return palindromic_partitions

# Read input from standard input
s = input()

# Call the function and print the result to standard output
print(partition_palindromes(s))
