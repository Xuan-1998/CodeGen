def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end-1]:
            return False
        start += 1
        end -= 1
    return True

def partition_palindrome(s, start=0, end=None):
    result = []
    if end is None:
        end = len(s)
    if start >= end:
        return [[]]
    for i in range(start, end-1):
        if is_palindrome(s, start, i+1):
            for p in partition_palindrome(s[:i], 0, i):
                result.append([s[i:]] + p)
    return result

S = input()
print(partition_palindrome(S))
