def min_cuts_palindrome(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:  # Palindromic check: even length or single character
                dp[i][j] = (length % 2 == 0) or dp[i + 1][j - 1]
            else:
                dp[i][j] = False

    cuts = 0
    for i in range(n):
        if not dp[0][i]:
            cuts += 1

    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts_palindrome(s))
