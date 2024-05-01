from functools import lru_cache

def count_ways_to_form_N(m, N):
    @lru_cache(None)
    def dp(N, i):
        if N == 0:
            return [1]
        ways = []
        for j in range(i+1):
            new_N = N - m[j-1]
            ways.extend([j] + way for way in dp(new_N, j))
        return ways

    result = []
    for i in range(1, m+1):
        result.extend(dp(N, i))
    return len(set(result)) % (10**9 + 7)

# Read input
m, N = map(int, input().split())
m = int(input())

print(count_ways_to_form_N(m, N))
