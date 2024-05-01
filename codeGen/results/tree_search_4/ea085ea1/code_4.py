def max_common_substrings(str1, str2):
    N = len(str1)
    dp = {}
    
    def find_max(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        if i == 0 or j == 0:
            result = 0
        elif str1[i-1] == str2[j-1]:
            result = 1 + find_max(i-1, j-1)
        else:
            result = max(N, min(find_max(i-1, j), find_max(i, j-1)))
        
        dp[(i, j)] = result
        return result
    
    return find_max(N, N)

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
