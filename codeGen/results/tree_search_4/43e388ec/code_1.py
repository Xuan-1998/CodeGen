from functools import lru_cache

a, b = map(int, input().split())
dp_dict = {0: 0}

@lru_cache(None)
def dp(i):
    if i - 1 not in dp_dict:
        dp_dict[i-1] = ((a >> (i-1)) | (b << i)) % (10**9+7)
    return dp_dict[i-1]

memoized_dp_sum = sum(dp(i) for i in range(314159))
print(memoized_dp_sum % (10**9+7))
