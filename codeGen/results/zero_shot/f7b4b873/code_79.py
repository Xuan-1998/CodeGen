def find_palindromic_partitions(S):
    partitions = []
    for i in range(1, len(S)):
        left = S[:i]
        right = S[i:]
        if is_palindrome(left) and is_palindrome(right):
            partitions.append([left, right])
    return partitions

def is_palindrome(s):
    return s == s[::-1]

# Read input from stdin
S = input()

# Call the function to find palindromic partitions
partitions = find_palindromic_partitions(S)

# Print the result to stdout
print(partitions)
