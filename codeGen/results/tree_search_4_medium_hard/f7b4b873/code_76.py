def partition_palindromes(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start, len(s)):
            substring = s[start:end+1]
            if is_palindrome(substring):
                backtrack(end+1, [substring] + path)

    result = []
    backtrack(0, [])
    return result

s = input()
print(partition_palindromes(s))
