def can_form_polygon(mood):
    memo = {}

    def dp(i, s):
        if (i, tuple(sorted(s))) in memo:
            return memo[(i, tuple(sorted(s)))]
        if i == len(mood) - 1:
            return 'YES' if len(s) == len(mood) - 1 else 'NO'
        if mood[i] == 0:
            return 'NO'
        next_s = s | {i}
        if len(next_s) == len(mood) - 1:
            return 'YES'
        result = dp(i + 1, next_s)
        memo[(i, tuple(sorted(s)))] = result
        return result

    return dp(0, set())
