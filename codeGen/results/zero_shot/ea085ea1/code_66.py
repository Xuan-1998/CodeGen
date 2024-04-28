N = int(input())
str1 = input().replace('\n', '')
str2 = input().replace('\n', '')

def common_substrings(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0
    last_occurrence = -1
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    last_occurrence = i
            else:
                dp[i][j] = 0
    
    common_substrings_count = 0
    while max_length > 0:
        for i in range(last_occurrence - max_length + 1, last_occurrence + 1):
            str1_common = str1[i-1:i-max_length+1]
            if str2.find(str1_common) != -1:
                common_substrings_count += 1
                break
        max_length -= 1
    
    print(common_substrings_count)
