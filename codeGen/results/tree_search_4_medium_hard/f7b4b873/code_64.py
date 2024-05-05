def palindromic_partitions(s):
    # Initialize an empty dictionary to store the results of subproblems
    dp = {}

    def is_palindrome(s):
        return s == s[::-1]

    def partition_recursive(s, prev_partition):
        if not s:
            return [prev_partition]
        
        partitions = []
        for i in range(len(s)):
            prefix = s[:i+1]
            suffix = s[i+1:]
            if is_palindrome(prefix + suffix):
                new_partition = [prefix] + prev_partition
                if not prefix or (prefix, new_partition) in dp:
                    continue
                partitions.extend(partition_recursive(suffix, new_partition))
        return partitions

    # Main function to generate all palindromic partitions
    def get_partitions(s):
        result = []
        for i in range(len(s)):
            prefix = s[:i+1]
            suffix = s[i+1:]
            if is_palindrome(prefix + suffix):
                new_partition = [prefix] + []
                result.extend(partition_recursive(suffix, new_partition))
        return result

    # Call the main function and print the result
    result = get_partitions(s)
    for partition in result:
        print(partition)

# Example usage:
s = input()
palindromic_partitions(s)
