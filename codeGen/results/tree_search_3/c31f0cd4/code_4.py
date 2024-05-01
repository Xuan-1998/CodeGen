import sys
from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    dp = defaultdict(int)
    result = set()
    
    for i in range(1 << n):
        temp_sum = 0
        subset_sum = 0
        
        for j in range(n):
            if ((i >> j) & 1):  # Check if the bit is on
                temp_sum += arr[j]
        
        for k in range(temp_sum + 1):
            if dp[k] and dp.get(k - temp_sum, False):
                result.add(k)
        
        dp[temp_sum] = True
    
    print(' '.join(map(str, sorted(list(result)))))

solve()
