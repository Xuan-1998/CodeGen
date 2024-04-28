def longest_palindrome(s):
    dp = {}

    def is_palindrome(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        if i >= j:
            return True

        if s[i] == s[j]:
            if i + 1 > j - 1 or is_palindrome(i + 1, j - 1):
                dp[(i, j)] = True
                return True
        else:
            dp[(i, j)] = False
            return False

    max_len = 0
    longest_pal = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    longest_pal = s[i:j+1]

    return longest_pal

# Read input from stdin
s = input()

# Print the output to stdout
print(longest_palindrome(s))
