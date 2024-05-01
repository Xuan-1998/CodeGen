def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [0] * N
    last_occurrence = [-1] * N

    for left in range(N):
        for right in range(left, N):
            if str1[left:right + 1] == str2[left:right + 1]:
                dp[right] = max(dp[right], dp[left - 1] + 1)
                last_occurrence[right] = right
            else:
                last_occurrence[right] = -1

    return max(dp)

str1 = input()
str2 = input()
print(max_common_substrings(str1, str2))
