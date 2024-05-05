from functools import lru_cache

n = int(input())
moods = [int(x) for x in input().split()]

@lru_cache(maxsize=None)
def dp(i, good):
    if i == 0:
        return "NO"
    if i == 1 and good:
        return "YES"
    result = "NO"
    max_good = 0
    regular = False
    for j in range(min(i, len(moods))):
        if moods[j]:
            max_good = max(max_good, j + 1)
            regular = max_good == i
        else:
            break
    return "YES" if regular else result

print("YES" if dp(n, True) else "NO")
