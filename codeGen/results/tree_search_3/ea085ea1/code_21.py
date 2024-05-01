def max_common_substrings(str1, str2):
    m = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    ans = 0
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
                ans = max(ans, m[i][j])
    
    return ans

# read input from stdin
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
