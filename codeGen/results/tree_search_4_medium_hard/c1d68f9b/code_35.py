from functools import lru_cache

def can_form_polygon(n, moods):
    @lru_cache(None)
    def dp(i):
        if i >= n // 2:  # Base case: one knight left
            return True
        j = (i - 1) % n
        if moods[i] == 0 and moods[j] == 0:
            return dp(j + 1)
        return False

    for i in range(n):
        if not dp(i):
            return "NO"
    return "YES"

n = int(input())
moods = [int(x) for x in input().split()]
print("YES" if can_form_polygon(n, moods) else "NO")
