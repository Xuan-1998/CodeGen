def is_scrambled(s1, s2):
    # Check if the strings have the same length
    if len(s1) != len(s2):
        return False

    # Compare characters at corresponding positions
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# Read input from stdin
s1 = input()
s2 = input()

# Print the answer to stdout
print(is_scrambled(s1, s2))
