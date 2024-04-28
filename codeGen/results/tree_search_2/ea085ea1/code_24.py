def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    # Create a 3D DP table to store the maximum number of common non-overlapping substrings
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j in range(i, N):
            for k in range(N):
                for l in range(k, N):
                    # Check if there is at least one common character between str1[i..j] and str2[k..l]
                    if all(x == y or x == '*' or y == '*' for x, y in zip(str1[i:j+1], str2[k:l+1])):
                        dp[j - i + 1][l - k + 1][len(set(str1[i:j+1]) & set(str2[k:l+1]))] = max(dp[j - i + 1][l - k + 1][len(set(str1[i:j+1]) & set(str2[k:l+1]))], dp[j - i][l - k][len(set(str1[i:j+1]) & set(str2[k:l+1]))] + 1, default=0)

    # The maximum number of common non-overlapping substrings is the length of the longest increasing subsequence
    return max(max(map(max, dp)), default=0)


print(find_common_substrings())
