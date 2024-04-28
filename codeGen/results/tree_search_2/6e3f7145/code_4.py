def longest_palindromic_substring(s):
    n = len(s)
    memo = {}

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(n):
        # Odd-length palindrome centered at position i
        memo[i, i] = s[i]
        for k in range(1, (n - i) // 2):
            if s[i:i+2*k+1] == s[i:i+2*k+1][::-1]:
                memo[i, i + 2*k] = s[i:i+2*k+1]

    # Find the longest palindromic substring
    max_len = 0
    longest_palindrome = ""
    for (i, j) in sorted(memo.keys()):
        if len(memo[i, j]) > max_len:
            max_len = len(memo[i, j])
            longest_palindrome = memo[i, j]

    return longest_palindrome
