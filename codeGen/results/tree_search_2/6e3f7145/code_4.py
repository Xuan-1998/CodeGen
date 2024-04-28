def longest_palindrome(s):
    memo = {}

    def is_palindrome(s, e):
        if (s, e) in memo:
            return memo[(s, e)]

        if s >= e:
            return True

        if s == e - 1:
            return s == len(s) - 1 or s == 0

        if s + 1 == e:
            return True

        mid = (s + e) // 2
        left, right = s + 1, e - 1

        while left <= right and s != e:
            if s == mid:
                left += 1
                right -= 1
            elif s < mid and mid < e:
                left += 1
            else:
                right -= 1

            if left > right:
                return False

        memo[(s, e)] = True if left >= right else is_palindrome(s + 1, e - 1)
        return memo[(s, e)]

    max_len = 0
    longest_pal = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(i, j) and j - i + 1 > max_len:
                max_len = j - i + 1
                longest_pal = s[i:j+1]

    return longest_pal

# Example usage:
s = input()
print(longest_palindrome(s))
