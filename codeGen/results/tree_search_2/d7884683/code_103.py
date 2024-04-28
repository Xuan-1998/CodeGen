import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        # Fill up the DP table
        for i in range(1, n + 1):
            left_sum = sum(arr[:i])
            right_sum = sum(arr[i:])
            if left_sum == right_sum:
                dp[i][i] = True
        
        # Traverse the array to find maximum partition count
        max_partition_count = 0
        for i in range(1, n + 1):
            if dp[i][i]:
                max_partition_count += 1
                i = n - 1  # Move to the next index
            while i > 0 and not dp[i][i]:
                i -= 1
        
        print(max_partition_count)

solve()
