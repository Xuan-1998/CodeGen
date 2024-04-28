import sys

def max_partitions(arr):
    n = len(arr)
    memo = {0: 1}
    
    def dp(i):
        if i in memo:
            return memo[i]
        
        total_sum = sum(arr[:i+1])
        left_sum = 0
        
        count = 0
        for j in range(1, i+1):
            left_sum += arr[j-1]
            right_sum = total_sum - left_sum
            
            if left_sum == right_sum:
                count += dp(j-1) + 1
            else:
                count += dp(j-1)
        
        memo[i] = max(count, 1)
        return memo[i]
    
    return dp(n-1)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
