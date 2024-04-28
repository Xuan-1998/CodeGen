s1 = input()
s2 = input()

def common_substrings(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    count = 0
    max_count = 0
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_count:
                    count = 0
                    for k in range(max_count):
                        if s1[i - 1 - k:i] == s2[j - 1 - k:j]:
                            count += 1
                    max_count = dp[i][j]
    
    return max_count

print(common_substrings(s1, s2))
