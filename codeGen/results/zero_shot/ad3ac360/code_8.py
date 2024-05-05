def min_cuts(s):
    n = len(s)
    cuts = 0
    for i in range(n - 1):
        is_palindrome = True
        left, right = i, n - i - 1
        while left < right:
            if s[left] != s[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
        if not is_palindrome:
            cuts += 1
    return cuts

# Read input from stdin
s = input()

# Calculate and print the result
print(min_cuts(s))
