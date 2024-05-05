import sys

def is_palindrome(s):
    return s == s[::-1]

def min_cuts_to_palindromes(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n):
        if is_palindrome(s[:i+1]):
            dp[i+1] = True

    cuts = 0
    for i in range(1, n+1):
        if not dp[i]:
            min_cuts = float('inf')
            for j in range(i):
                if dp[j] and dp[i-j-1]:
                    min_cuts = min(min_cuts, min_cuts_to_palindromes(s[j:i]))
            cuts += min_cuts

    return cuts + 1

if __name__ == '__main__':
    s = input().strip()
    print(min_cuts_to_palindromes(s))
