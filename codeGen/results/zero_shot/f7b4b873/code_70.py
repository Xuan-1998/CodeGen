def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(s):
    partitions = []
    def dfs(s, path):
        if not s:
            partitions.append(path)
            return
        for i in range(1, len(s)+1):
            if is_palindrome(s[:i]):
                dfs(s[i:], path + [s[:i]])
    dfs(s, [])
    return partitions

n = int(input())
s = input()
print(palindromic_partitions(s))
