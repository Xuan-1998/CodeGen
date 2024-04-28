from functools import lru_cache

def find_subset_sum(n, m):
    @lru_cache(None)
    def dfs(i, s):
        if s % m == 0:
            return True
        for j in range(i, n):
            if (s + j) % m == 0 or dfs(j, s + j):
                return True
        return False

    for i in range(n):
        if dfs(i, i):
            return 1
    return 0

n = int(input())  # number of elements
m = int(input())  # value
numbers = list(map(int, input().split()))  # array of n non-negative integers
print(find_subset_sum(n, m))
