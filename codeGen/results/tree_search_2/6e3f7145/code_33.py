def longest_palindrome(s):
    n = len(s)
    p = [0] * n  # Initialize the state expression array
    max_length = 0
    center_index = 0

    for i in range(n):  # Iterate through each character in the string
        if i < n // 2:  # Check if we're at or before the midpoint
            p[i] = min(p[2 * i - (i >= n // 2)], i + 1)  # Update p[i]
        else:
            p[n - i - 1] = min(p[2 * n - 2 * i - 1], i + 1)  # Update p[n-i-1]

        while True:  # Expand around the center
            if s[i - p[i]] != s[i + p[i]]:
                break
            p[i] += 1

        if p[i] > max_length:
            max_length = p[i]
            center_index = i

    return s[center_index - max_length: center_index + max_length]

# Test the function with a sample string
s = "babad"
print(longest_palindrome(s))  # Output: "bab"

