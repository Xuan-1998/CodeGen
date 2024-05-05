def is_palindrome(s, i, j):
    if i >= j:  # single character or empty string
        return True
    if s[i] != s[j]:  # characters don't match
        return False
    return is_palindrome(s, i+1, j-1)  # recursive check

def min_cuts_to_palindromes(s):
    n = len(s)
    dp = [[0] * (n-1) for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0  # single-character strings are always palindromes
        if i > 0:
            dp[0][i] = i  # prefix is not a palindrome, so we need to cut at each character

        for j in range(i-1, -1, -1):
            if s[j] != s[i]:  # characters don't match
                dp[j][i] = min(dp[j][k] + dp[k+1][i] for k in range(j, i)) + 1
            else:  # substring is a palindrome
                dp[j][i] = dp[j+1][i-1]

    return dp[0][n-2]  # answer is stored at the bottom-right corner

def main():
    s = input()  # read input string from stdin
    print(min_cuts_to_palindromes(s))  # output minimum number of cuts to stdout

if __name__ == "__main__":
    main()
