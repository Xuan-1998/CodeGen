def longest_palindrome(s):
    n = len(s)
    memo = {}

    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        k = abs(j - i)
        if k <= 0:
            return True
        if s[i] != s[j]:
            return False
        memo[(i, j)] = is_palindrome(i + 1, j - 1)
        return memo[(i, j)]

    max_length = 0
    longest_pal = ""
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j) and j - i + 1 > max_length:
                max_length = j - i + 1
                longest_pal = s[i:j+1]
    return longest_pal

if __name__ == "__main__":
    s = input()
    print(longest_palindrome(s))
