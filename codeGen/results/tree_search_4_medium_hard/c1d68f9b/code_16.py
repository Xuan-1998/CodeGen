def can_form_polygon(moods):
    n = len(moods)
    memo = {}

    def dp(i, max_good_moods):
        if i == n:
            return "YES" if max_good_moods % n == 0 else "NO"
        if (i, max_good_moods) in memo:
            return memo[(i, max_good_moods)]
        if moods[i] == 1:
            result = dp(i + 1, max_good_moods + 1)
        else:
            result = "NO" if max_good_moods > 0 else "YES"
        memo[(i, max_good_moods)] = result
        return result

    return dp(0, 0)

n = int(input())
moods = list(map(int, input().split()))
print(can_form_polygon(moods))
