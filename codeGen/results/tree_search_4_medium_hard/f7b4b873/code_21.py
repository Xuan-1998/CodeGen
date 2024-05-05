def partition_palindromic(s):
    def is_palindrome(s):
        return s == s[::-1]

    n = len(s)
    dp = {}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        if i >= j or not is_palindrome(s[i:j+1]):
            return [[]]
        
        result = []
        for k in range(i, j+1):
            if is_palindrome(s[i:k+1]) and is_palindrome(s[k:j+1]):
                for p in dfs(k+1, j):
                    result.append([s[i:k+1]] + p)
        
        dp[(i, j)] = result
        return result

    return dfs(0, n-1)

if __name__ == "__main__":
    s = input()
    print(partition_palindromic(s))
