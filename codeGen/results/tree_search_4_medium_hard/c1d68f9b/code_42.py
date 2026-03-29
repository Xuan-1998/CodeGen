def can_form_polygon(moods):
    n = len(moods)
    memo = {}

    def dfs(s, k):
        if (s, k) in memo:
            return memo[(s, k)]
        if len(s) == n - 1:
            return True
        if moods[k] == 0:
            return False
        next_s = s | {k}
        result = any(dfs(next_s, i) for i in range(n) if i != k and moods[i] == 1)
        memo[(s, k)] = result
        return result

    return 'YES' if dfs(set(), n - 1) else 'NO'

moods = [int(x) for x in input().split()]
print(can_form_polygon(moods))
