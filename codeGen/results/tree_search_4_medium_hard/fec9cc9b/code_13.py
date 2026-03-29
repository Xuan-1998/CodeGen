import sys
from collections import memoize

@memoize
def dp(i):
    if i == 0:
        return True
    max_non_decreasing = False
    for j in range(i):
        if array[j] <= array[i]:
            max_non_decreasing |= dp(j)
    return max_non_decreasing

n, m = map(int, input().split())
array = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    if array[l-1:r] == array[:r-l+1]:
        print("Yes")
    else:
        print("No")
