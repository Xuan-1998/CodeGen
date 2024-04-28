import sys
from collections import defaultdict

def solve(m, N):
    dp = defaultdict(int)
    dp[(0, m)] = 1  # Base case: no elements left, sum is 0
    
    for i in range(1, m + 1):
        for j in range(i, -1, -1):  # Iterate over all possible sums
            if j > N:
                break
            dp[(j, i)] += dp[(j - i, i)]
    
    return dp[(N, 0)] % (10**9 + 7)

m, N = map(int, input().split())
print(solve(m, N))
