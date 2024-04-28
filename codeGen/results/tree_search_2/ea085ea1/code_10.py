from collections import defaultdict

def max_common_substrings(str1, str2):
    dp = defaultdict(int)
    
    for i in range(len(str1)):
        for j in range(i+1):
            if str1[i:j+1] == str2[-(j+1):i+1]:
                dp[(i, j)] = 1
            else:
                dp[(i, j)] = max(dp.get((i-1, j), 0), dp.get((i, j-1), 0)) + 1
                
    return max(max(row) for row in dp.values())
