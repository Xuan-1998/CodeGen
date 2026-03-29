def min_cuts(s):
    memo = {}

    def helper(i):
        if i >= len(s):
            return 0
        
        if (i, 'yes') in memo:
            return memo[(i, 'yes')]
        
        if (i, 'no') in memo:
            return memo[(i, 'no')]
        
        is_palindrome = s[i] == s[-1 - i]
        
        if is_palindrome:
            result = 0
        else:
            result = 1
        
        for j in range(i):
            if s[j] != s[-1 - j]:
                if not is_palindrome:
                    break
                else:
                    j += 1
            else:
                continue
            
            result += 1
        
        memo[(i, 'yes')] = helper(i + 1)
        memo[(i, 'no')] = result
        
        return min(result, memo[(i, 'no')])

    return helper(0)

print(min_cuts(input()))
