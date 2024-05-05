def partition(s):
    memo = {}
    
    def helper(s, p):
        if s == '':
            return [p]
        if (s, p) in memo:
            return memo[(s, p)]
        
        result = []
        for i in range(1, len(s)):
            t = s[:i]
            u = s[i:]
            if t == t[::-1]:
                partitions = helper(u, [t] + p)
                result += [[t]] + partitions
        memo[(s, p)] = result
        return result
    
    return helper(s, [])

print(partition(input()))
