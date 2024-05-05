from sys import stdin

def can_reach_last_index(arr):
    n = len(arr)
    dp = [False] * n
    
    # Base case: we can always reach the first element
    dp[0] = True
    
    for i in range(1, n):
        for j in range(max(0, i-arr[i]), -1, -1):
            if dp[j]:
                dp[i] = True
                break
    
    return dp[-1]

# Read the array from stdin
arr = list(map(int, stdin.readline().split()))

# Print the answer to stdout
print(can_reach_last_index(arr))
