import sys

def is_palindrome(s):
    return s == s[::-1]

def find_partitions(s):
    n = len(s)
    partitions = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partition = s[i - 1:j]
            if is_palindrome(partition):
                partitions.append([partition])
    return [p + [s] for p in partitions]

S = input()
print(find_partitions(S))
