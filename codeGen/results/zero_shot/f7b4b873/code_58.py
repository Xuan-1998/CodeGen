def find_partitions(s):
    partitions = []
    def recursive_find_partitions(s, current_partition):
        if not s:  # base case: empty string
            partitions.append(current_partition)
            return
        for i in range(len(s)):
            substring = s[:i+1]
            if substring == substring[::-1]:  # palindrome check
                recursive_find_partitions(s[i+1:], current_partition + [substring])
    recursive_find_partitions(s, [])
    return partitions

# Example usage:
S = input()  # read string from stdin
partitions = find_partitions(S)
print(partitions)  # print the result to stdout
