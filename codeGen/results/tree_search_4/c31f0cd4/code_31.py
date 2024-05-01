import sys
from collections import defaultdict

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    dp = [[False] * (sum(nums) + 1) for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, n+1):
        for j in range(sum(nums) + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    sums = set()
    for j in range(sum(nums) + 1):
        if dp[n][j]:
            sums.add(j)
    
    print(' '.join(map(str, sorted(list(sums)))))

if __name__ == "__main__":
    solve()
