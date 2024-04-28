def longest_palindromic_substring():
    s = input()  # Receive the input string from stdin

    n = len(s)
    dp = [[False] * n for _ in range(n)]

    max_length = 0
    center = 0

    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i < 2:  # Single character or two adjacent characters
                    dp[i][j] = True
                    max_length = 1
                    center = i
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False

    longest_palindrome = s[center - max_length: center + max_length]

    print(longest_palindrome)  # Print the answer to stdout
