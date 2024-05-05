def is_palindrome(s):
    return s == s[::-1]

def partition_palindromes(S):
    def backtrack(start, path):
        if start == len(S):
            result.append(path)
            return
        for end in range(start, len(S)):
            if is_palindrome(S[start:end+1]):
                backtrack(end + 1, path + [S[start:end+1]])
    result = []
    backtrack(0, [])
    return result

S = input()
print(partition_palindromes(S))
