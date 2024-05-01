from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, s):
    if i == 0:
        return [s]
    result = []
    for j in range(i+1):
        for subset_sum in dp(j, 0):
            result.append(s + subset_sum)
    return list(set(result))

n = int(input())
nums = list(map(int, input().split()))
result = dp(n, 0)
print(' '.join(map(str, sorted(result))))
