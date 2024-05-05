def min_cuts_to_palindrome(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n + 1):
        dp[i] = True

    cuts = 0
    for i in range(1, n):
        for j in range(i):
            if s[j:i+1] == s[i:j:-1]:  # Check if substring is palindromic
                dp[i] = True
                break
        if not dp[i]:
            cuts += 1

    return cuts + 1  # Add 1 because we need to cut at the end of the string as well

s = input()
print(min_cuts_to_palindrome(s))
