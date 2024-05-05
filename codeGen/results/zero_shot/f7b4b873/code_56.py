def palindromic_partitions(S):
    def is_palindrome(s):
        return s == s[::-1]

    def partition(s):
        if not s:
            return [[]]
        partitions = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if is_palindrome(prefix):
                for p in partition(suffix):
                    partitions.append([prefix] + p)
        return partitions

    result = partition(S)
    return [p for p in result if is_palindrome(''.join(p))]

import sys
S = input()
print(palindromic_partitions(S))
