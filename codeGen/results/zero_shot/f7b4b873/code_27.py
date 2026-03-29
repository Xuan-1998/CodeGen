def partition_palindromes(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    result = []
    for i in range(1, len(s)):
        for j in range(i, 0, -1):
            partition = s[:j]
            if is_palindrome(partition):
                result.append([partition])
                for k in range(j, len(s)):
                    partition += s[k]
                    if is_palindrome(partition):
                        result[-1].append(partition)
    return result

s = input()
print(partition_palindromes(s))
