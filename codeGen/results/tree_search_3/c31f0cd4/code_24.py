from functools import lru_cache

@lru_cache(maxsize=None)
def count_ways(remaining_integers):
    if not remaining_integers:
        return 1
    total = sum(remaining_integers)
    dp = {}
    for i in range(total + 1):
        dp[i] = 0
    dp[0] = 1
    for integer in remaining_integers:
        for sum in range(i := integer, -1, -1):
            if (new_sum := sum + integer) <= total:
                dp[new_sum] += dp.get(sum, 0)
    return dp

N = int(input())
numbers = list(map(int, input().split()))
all_sums = set()
for mask in range(2 ** N):
    subset = [num for i, num in enumerate(numbers) if (mask & (1 << i)) > 0]
    total = sum(subset)
    all_sums.add(total)

print(*sorted(all_sums), sep=' ')
