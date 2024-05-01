from functools import lru_cache
def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    
    @lru_cache(None)
    def dp(i, s):
        if i < 0:
            return not bool(s)  # base case: sum is 0 if and only if we're at the beginning of the array
        if s == 0:
            return True  # base case: we can always get a sum of 0 by not including any numbers
        res = False
        for j in range(i, -1, -1):
            if dp(j, s - numbers[i]):
                res = True
                break
        return res
    
    sums = set()
    for i in range(n):
        for j in range(2**i):  # iterate through all possible subsets of previous numbers
            subset_sum = sum(num for k, num in enumerate(numbers[:i]) if (j & (1 << k)))
            if dp(i, subset_sum):  # check if the calculated sum is present in the memoized dictionary
                sums.add(subset_sum)
    
    print(*sorted(sums), sep=' ')
