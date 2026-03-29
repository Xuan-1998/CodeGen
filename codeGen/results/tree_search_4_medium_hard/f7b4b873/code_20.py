def partition_palindromes(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return [[]]
        
        result = []
        for k in range(i, j + 1):
            if is_palindrome(s[i:k+1]):
                for p in dfs(k+1, j):
                    result.append([s[i:k+1]] + p)
        memo[(i, j)] = result
        return result

    return dfs(0, len(s) - 1)

print(partition_palindromes(input()))
