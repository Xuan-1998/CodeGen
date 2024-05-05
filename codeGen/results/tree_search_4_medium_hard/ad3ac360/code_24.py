import sys

def min_cuts_to_palindrome(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:
                dp[i][j - 1] = dp[i + 1][j - 2]
            else:
                dp[i][j - 1] = False

    cuts = 0
    for i in range(1, n):
        if not dp[0][i]:
            cuts += 1

    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts_to_palindrome(s))
