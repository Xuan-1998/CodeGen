def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    def expand_around_center(left, right):
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1

        if is_palindrome(s[left:right+1]):
            return [s[left:right+1]]

    result = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j+1]):
                for k in range(j+1, len(s)):
                    if s[k] == s[j]:
                        partition = expand_around_center(i, k)
                        result.extend([s[:i] + ' '.join(partition) + s[k+1:]] if partition else [])

    return result
