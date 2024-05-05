def partition_palindromes(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def recursive_partition(s, prefix_partitions):
        if len(s) <= 1:
            return [prefix_partitions]
        
        palindromic_partitions = []
        for i in range(len(s)):
            suffix = s[i+1:]
            if is_palindrome(s[:i+1]):
                partitions = recursive_partition(suffix, [s[:i+1]] + prefix_partitions)
                palindromic_partitions.extend(partitions)
        
        return palindromic_partitions

    return recursive_partition(s, [])

# Receive input from stdin
s = input()

# Print the output to stdout
print(partition_palindromes(s))
