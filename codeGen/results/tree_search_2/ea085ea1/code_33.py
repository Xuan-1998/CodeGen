def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N):
        for j in range(i + 1):
            k = N - 1
            while k >= j:
                if str1[i] == str2[k]:
                    dp[j][i] += 1
                    break
                k -= 1
    
    max_count = 0
    for i in range(N):
        for j in range(i + 1):
            max_count = max(max_count, dp[j][i])
    
    return max_count

# Example usage:
str1 = input()
str2 = input()
print(max_common_substrings(str1, str2))
