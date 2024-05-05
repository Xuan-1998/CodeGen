def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(S):
    N = len(S)
    result = []
    
    def partition(s, path):
        if not s:
            result.append(path)
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if is_palindrome(prefix):
                partition(suffix, [path] + [prefix])
    
    partition(S, [])
    return result

S = input()
print(palindromic_partitions(S))
