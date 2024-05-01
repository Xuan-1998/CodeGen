def max_common_substrings():
    N = int(input())
    str1 = input()
    str2 = input()

    dp = [[False] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                if i == 1 or j == 1:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False

    max_length = 0
    count = 0
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if dp[i][j]:
                length = i
                while True:
                    str1_substring = str1[:i]
                    str2_substring = str2[:j]
                    if str1_substring not in str2 or str2_substring not in str1:
                        break
                    count += 1
                    i -= 1
                    j -= 1
                max_length = max(max_length, length)
    print(count)

max_common_substrings()
