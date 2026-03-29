def palindromic_partitions(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def partition_string(s, current_partition=[]):
        if not s:
            partitions.append(current_partition)
        else:
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                suffix = s[i:]
                if is_palindrome(prefix + suffix):
                    partition_string(suffix, current_partition + [prefix])

    partitions = []
    partition_string(s)
    return partitions

if __name__ == "__main__":
    s = input()  # read the input string from stdin
    partitions = palindromic_partitions(s)
    print(partitions)  # print the result to stdout
