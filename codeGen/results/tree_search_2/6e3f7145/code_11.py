def longest_palindromic_substring(S):
    memo = {}

    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        substring = S[i:j+1]
        if substring == substring[::-1]:
            return True
        else:
            return False

    max_length = 0
    longest_palindrome = ""

    for i in range(len(S)):
        for j in range(i, len(S)):
            if is_palindrome(i, j):
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    longest_palindrome = S[i:j+1]

    return longest_palindrome

S = input()
print(longest_palindromic_substring(S))
