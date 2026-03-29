def palindromic_partitions(S):
    def is_palindrome(s):
        return s == s[::-1]

    def partition(s, partitions=None):
        if not s:
            return [partitions]
        partitions = partitions or []
        for i in range(1, len(s) + 1):
            substr = s[:i]
            if is_palindrome(substr):
                new_partitions = partition(s[i:], partitions + [[substr]])
                if new_partitions:
                    return new_partitions
        return []

    result = []
    for i in range(1, len(S) + 1):
        substr = S[:i]
        if is_palindrome(substr):
            result.extend(partition(S[i:], [[substr]]))
    return result

# Read input from stdin
S = input()

# Print the output to stdout
print(palindromic_partitions(S))
