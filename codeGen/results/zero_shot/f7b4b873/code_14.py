def is_palindrome(s):
    return s == s[::-1]

def get_partitions(s):
    if len(s) == 0:
        return [[]]
    
    partitions = []
    for i in range(1, len(s)):
        prefix = s[:i]
        suffix = s[i:]
        if is_palindrome(prefix + suffix):
            for p in get_partitions(suffix):
                partitions.append([prefix] + p)
    
    return partitions

n = int(input())
s = input()
print(get_partitions(s))
