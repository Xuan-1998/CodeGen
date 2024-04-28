def longest_palindrome(S):
    n = len(S)
    dp = [False] * (n + 1)

    for i in range(n // 2):
        left, right = i, n - 1 - i
        while left < right:
            if S[left] != S[right]:
                break
            left += 1
            right -= 1

        dp[i*2+1] = True
        dp[n-1-i*2] = True
        while left >= 0 and right < n and S[left] == S[right]:
            dp[2*left+right+1] = True
            left -= 1
            right += 1

    max_length = 0
    result = ""
    for i in range(n):
        if dp[i]:
            j = i
            while j < n and not dp[j+1]:
                j += 1
            if j - i + 1 > max_length:
                max_length = j - i + 1
                result = S[i:j+1]

    return result

S = input()
print(longest_palindrome(S))
