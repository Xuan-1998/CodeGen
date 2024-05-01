import sys
from functools import lru_cache

@lru_cache(None)
def dp(subset, total):
    if total == 0:
        return True
    if total < 0 or not subset:
        return False
    if subset & 1:
        return dp(subset >> 1, total - 1) or dp(subset >> 1, total)
    return dp(subset >> 1, total)

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    sums = set()
    for subset in range(2 ** n):
        curr_sum = 0
        for i in range(n):
            if (subset & (1 << i)):
                curr_sum += nums[i]
        if dp(subset, curr_sum):
            sums.add(curr_sum)
    print(' '.join(map(str, sorted(sums))))

if __name__ == "__main__":
    solve()
