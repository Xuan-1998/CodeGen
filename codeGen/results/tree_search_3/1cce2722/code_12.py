import sys
from collections import defaultdict

def max_points_earned(a):
    memo = defaultdict(int)
    n = len(a)

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 0
        if a[i] not in (a[j-1], a[j+1]) for j in range(1, i):
            # If the current element is unique, we can delete it and all its neighbors.
            points = dp(i-3) + (i-2)
        else:
            # Otherwise, we should not delete this element or any of its neighbors.
            points = dp(i-1)
        memo[i] = points
        return points

    max_points = 0
    for i in range(n):
        max_points = max(max_points, dp(i))
    return max_points


n = int(input())
a = [int(x) for x in input().split()]
print(max_points_earned(a))
