def palindromic_partitions(s):
    if not s:
        return [[]]

    result = []
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if prefix == prefix[::-1]:  # check if prefix is a palindrome
            for partition in palindromic_partitions(s[i:]):
                result.append([prefix] + partition)
    
    return result

import sys
s = input().strip()
print(palindromic_partitions(s))
