def longest_palindromic_substring(s):
    memo = {}
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i > j:
            return ""
        
        if s[i] == s[j]:
            if j - i < 2:
                return s[i:j+1]
            else:
                result = helper(i + 1, j - 1)
                if len(result) > 0 and s[i] == result[0] and s[j] == result[-1]:
                    return s[i:j+1]
        else:
            result1 = helper(i + 1, j)
            result2 = helper(i, j - 1)
            if len(result1) > len(result2):
                return result1
            else:
                return result2
        
        memo[(i, j)] = result1
        return result1
    
    return max(helper(0, i) for i in range(len(s)))
