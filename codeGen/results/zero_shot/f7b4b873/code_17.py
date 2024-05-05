def is_palindrome(s):
    return s == s[::-1]

def partition(s, start_index=0):
    if start_index == len(s):
        return [[]]  # base case: empty string has one partition (the empty list)

    partitions = []
    for end_index in range(start_index, len(s)):
        substring = s[start_index:end_index+1]
        if is_palindrome(substring):
            if end_index == len(s) - 1:
                partitions.append([substring])  # single-word palindrome
            else:
                remaining_partitions = partition(s, end_index+1)
                for p in remaining_partitions:
                    p.insert(0, substring)
                    partitions.append(p)

    return partitions

import sys

# Read input from stdin
S = sys.stdin.readline().strip()

# Generate and print all palindromic partitions
partitions = partition(S)
for p in partitions:
    print(p)
