def longest_palindrome(s):
    n = len(s)
    dp = [""] * (n + 1)

    for i in range(n):
        if i % 2 == 0:
            dp[i + 1] = dp[i]
        else:
            left, right = i - 1, i
            while left >= 0 and right < n and s[left] == s[right]:
                dp[i + 1] = dp[i]
                left -= 1
                right += 1

    max_len = 0
    result = ""
    for i in range(n):
        if len(dp[i]) > max_len:
            max_len = len(dp[i])
            result = dp[i]

    return result

# Example usage:
s = input()
print(longest_palindrome(s))
