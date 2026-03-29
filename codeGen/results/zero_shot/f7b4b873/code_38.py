def partition(s):
    result = []
    def helper(s, path, start):
        if not s:
            result.append(path)
            return
        for i in range(start, len(s)):
            palindrome = s[:i+1][::-1] == s[:i+1]
            if palindrome:
                helper(s[i+1:], path + [s[:i+1]], 0)
    helper(s, [], 0)
    return result

# Example usage
s = input()
result = partition(s)
for partition in result:
    print(partition)

