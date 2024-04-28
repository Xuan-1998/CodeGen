def longest_palindrome(s):
    memo = {}

    def is_palindrome(s, e):
        if (s, e) in memo:
            return memo[(s, e)]
        if s == e:
            return True  # single character is always palindromic

        if s + 1 == e or s >= len(s) - e:  # base case: length 1
            return s == e and s < len(s) // 2 and s > len(s) // 2 - 1

        if s == len(s) - e:  # middle character check
            if s % 2 == 0:
                memo[(s, e)] = is_palindrome(s // 2 - 1, e - (s // 2)) and True
            else:
                memo[(s, e)] = is_palindrome((s + 1) // 2 - 1, e - ((s + 1) // 2)) and s == e
        elif s < len(s) - e:  # non-middle character check
            if s % 2 == 0:
                memo[(s, e)] = is_palindrome(s // 2 - 1, e - (s // 2)) and s == e
            else:
                memo[(s + 1) // 2 - 1, e - ((s + 1) // 2)] = True

        return memo[(s, e)]

    max_len = 0
    longest_pal = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(i, j - 1):
                if j - i > max_len:
                    max_len = j - i
                    longest_pal = s[i:j]

    return longest_pal


# Example usage
s = input()
print(longest_palindrome(s))
