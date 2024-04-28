def longest_palindrome(s):
    n = len(s)
    dp = {i: 0 for i in range(n)}
    max_length = 0

    for i in range(1, n):
        if s[i-1] == s[i]:
            if i == 1 or s[i-2] != s[i]:
                dp[i] = dp[i-1] + 2
            else:
                dp[i] = dp[i-2] + 3

            max_length = max(max_length, dp[i])
        elif s[i-1] == s[i]:
            dp[i] = dp[i-1] + 2
            max_length = max(max_length, dp[i])

    return s[dp.index(max_length):max_length//2].__reversed__().join([s[dp.index(max_length)]]).ljust(max_length,"")

# Test the function
s = input()
print(longest_palindrome(s))
