def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = []
    memo = {}

    def dfs(start, end):
        if (start, end) in memo:
            return memo[(start, end)]
        if start >= end:
            return [[s[start:end+1]]]
        result = []
        for i in range(start, end+1):
            if is_palindrome(s[start:i+1]):
                for p in dfs(i+1, end):
                    result.append([s[start:i+1]] + p)
        memo[(start, end)] = result
        return result

    partitions = dfs(0, len(s)-1)
    return [p for ps in partitions for p in (ps if len(ps) > 1 else [' '.join(ps)])]

print(partition_palindromes(input()))
