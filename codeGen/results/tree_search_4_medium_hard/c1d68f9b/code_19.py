def can_form_polygon(n, moods):
    memo = {}

    def dfs(k, s):
        if (k, s) in memo:
            return memo[(k, s)]

        if k < 3:  # base case: at most two knights with good moods
            return "YES" if all(moods[i] for i in range(s)) else "NO"

        result = "NO"
        for i in range(k):
            if moods[i] and (k - 1) % (i + 1) == 0:  # consecutive good moods
                result = dfs(i, s)
                break

        memo[(k, s)] = result
        return result

    return "YES" if dfs(n - 1, 0) else "NO"
