def longest_palindrome(S):
    n = len(S)
    memo = {}

    def is_palindrome(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= j:
            return True
        if S[i] != S[j]:
            return False
        memo[(i, j)] = S[i+1:j-1].upper() == S[i+1:j-1].reverse().upper()
        return memo[(i, j)]

    longest = ""
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(i, j) and len(S[i:j+1]) > len(longest):
                longest = S[i:j+1]
    return longest

S = input()
print(longest_palindrome(S))
