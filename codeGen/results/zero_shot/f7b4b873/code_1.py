def palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start, len(s)):
            segment = s[start:end+1]
            if is_palindrome(segment):
                backtrack(end+1, path + [segment])

    result = []
    backtrack(0, [])
    return result

s = input()
print(palindromic_partitions(s))
