def min_cuts(s):
    n = len(s)
    cuts = 0

    for i in range(n):
        for j in range(i + 1, n):
            substring = s[i:j+1]
            if not is_palindrome(substring):
                cuts += 1
                break

    return cuts

def is_palindrome(substring):
    return substring == substring[::-1]

# Read input from stdin
s = input()

# Calculate the minimum number of cuts
cuts = min_cuts(s)

# Print the output to stdout
print(cuts)
