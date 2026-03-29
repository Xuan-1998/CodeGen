def partition(s):
    n = len(s)
    dp = [[[[] for _ in range(n)] for _ in range(n)] for _ in range(n)]

    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(i, j, partition):
        if i >= j:
            return [partition]
        result = []
        for k in range(i, j + 1):
            if is_palindrome(i, k - 1) and is_palindrome(k + 1, j):
                new_partition = partition + [[s[i:k]]]
                result.extend(dfs(k, j, new_partition))
        return result

    return dfs(0, n - 1, [[]])
