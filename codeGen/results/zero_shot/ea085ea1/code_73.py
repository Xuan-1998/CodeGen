n = int(input())
str1 = input().strip()
str2 = input().strip()

def find_common_substrings(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0
    result = 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if dp[i][j] == max_length:
                result += 1
                i -= max_length
                j -= max_length

    return result

print(find_common_substrings(str1, str2))
