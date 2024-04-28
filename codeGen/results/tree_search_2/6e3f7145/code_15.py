def longest_palindrome(s):
    n = len(s)
    memo = {}

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            if (left, right) not in memo:
                memo[(left, right)] = True
            left -= 1
            right += 1

    longest_palindrome_substring = ""

    for i in range(n):
        # Odd length palindrome
        expand_around_center(i, i)
        # Even length palindrome
        expand_around_center(i, i + 1)

    for (left, right) in sorted(memo.keys()):
        if len(s[left:right+1]) > len(longest_palindrome_substring):
            longest_palindrome_substring = s[left:right+1]

    return longest_palindrome_substring

s = input()
print(longest_palindrome(s))
