===BEGIN SOLUTION===
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return j == 0
    included = (j + arr[i - 1]) % m == 0 and dp(i - 1, j + arr[i - 1])
    excluded = dp(i - 1, j)
    return included or excluded

m, n = map(int, input().split())
arr = list(map(int, input().split()))
result = "Yes" if any(dp(n, i) for i in range(m + 1)) else "No"
print(result)

===END SOLUTION===
