from collections import defaultdict

def max_bitwise_or(s):
    n = len(s)
    memo = defaultdict(int)

    def dfs(i, j):
        if i > j:
            return 0
        key = (i, j)
        if (key in memo):
            return memo[key]
        result = i
        for k in range(i + 1, j + 1):
            or_value = int(s[i:k+1], 2) | int(s[k:j+1], 2)
            result = max(result, dfs(k, j))
        memo[key] = result
        return result

    return dfs(0, n - 1)

n = int(input())
s = input()
print(max_bitwise_or(s))
