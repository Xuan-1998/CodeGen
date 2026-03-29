code
def find_palindromic_partitions(s):
    dp = {}
    def dfs(s, p=[]):
        if not s:
            return [p]
        for i in range(len(s)):
            t = s[:i+1]
            if t == t[::-1]:
                result = dfs(s[i+1:], p + [t])
                if result:
                    dp[(s, i)] = result
                    return result
        return []
    return dfs(s)
