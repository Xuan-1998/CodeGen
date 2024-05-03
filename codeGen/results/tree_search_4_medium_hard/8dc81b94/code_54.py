from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if i == n - 1:
        return all(a[i] == 0 for a in array)

    left_sum = sum(array[:i])
    right_sum = sum(array[i:])

    return dp(i - 1) and (left_sum == right_sum or left_sum + n - i <= right_sum)

n, = map(int, input().split())
array = list(map(int, input().split()))
print("YES" if dp(0) else "NO")
