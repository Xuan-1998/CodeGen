def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    memo = {}
    for i in range(len(s)):
        if s[i] not in memo:
            memo[s[i]] = []
        memo[s[i]].append(i)

    longest_palindrome = ""
    for char, indices in memo.items():
        for i in range(len(indices) - 1):
            for j in range(i + 1, len(indices)):
                substring = s[indices[i]:indices[j] + 1]
                if substring == substring[::-1]:
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring

    return longest_palindrome


s = input()
print(longest_palindrome(s))
