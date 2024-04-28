def longest_palindrome(S):
    n = len(S)
    dp = [0] * (n * 2 - 1)

    for i in range(n):
        for j in range(i, n + i):
            mid = j // 2
            if S[j % 2 == 0 and j > 0: S[j//2-1:j//2+1]] == [S[n-j%2:n] and len(S) < 2:
                dp[j] = 2
            else:
                dp[j] = 1

    max_len = 0
    for i in range(n * 2 - 1):
        if dp[i] > max_len:
            max_len = dp[i]

    return S[n-max_len:n+max_len].lstrip()

S = input()
print(longest_palindrome(S))
