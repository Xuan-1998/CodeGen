import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Initialize memoization table with negative infinity
        dp = [[float('-inf') for _ in range(n+1)] for _ in range(n+1)]
        
        # Base case: partitioning an empty array is impossible
        dp[0][0] = 0
        
        total_sum = sum(arr)
        left_sum = 0
        count = 0
        
        for i in range(1, n+1):
            left_sum += arr[i-1]
            right_sum = total_sum - left_sum
            
            # If the current partition matches a previously seen one, update dp table
            if right_sum in [left_sum - x for x in dp[:i]]:
                dp[i][0] = max(dp[i][0], dp[:i].index(left_sum - right_sum) + 1)
            
            # Update dp table for the current partition
            for j in range(i-1, -1, -1):
                if left_sum - arr[j] >= right_sum and dp[i][j+1] > dp[i-1][j]:
                    dp[i][j] = dp[i-1][j] + 1
                    break
            
        print(dp[n][0])

if __name__ == "__main__":
    solve()
