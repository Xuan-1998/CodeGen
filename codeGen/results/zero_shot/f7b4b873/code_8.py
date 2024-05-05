def partition(s):
    if len(s) == 0:  # base case: empty string
        return [[]]  # single-element list containing an empty list

    partitions = []  # store all possible palindromic partitions
    for i in range(len(s)):
        # consider the current character as the center of a palindrome
        left, right = s[:i], s[i:]
        if left == left[::-1] and right == right[::-1]:  # both sides are palindromes
            new_partition = [left, right]
            for p in partition(right):  # recursively partition the remaining string
                partitions.append([s[:i]] + p)
    return partitions

# receive input from stdin
S = input()

# find all possible palindromic partitions of S
partitions = partition(S)

# print the result to stdout
for p in partitions:
    print(p)
