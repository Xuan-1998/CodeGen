import sys

def canJump(arr):
    n = len(arr)
    dp = {i: False for i in range(n)}
    
    # Handle edge case where array is empty
    if not arr:
        return True
    
    # Handle edge case where array has only one element
    if n == 1:
        return True
    
    dp[0] = True
    
    for i in range(1, n):
        if dp[i - 1]:
            for j in range(i - 1, -1, -1):
                if arr[j] >= i - j and dp[j]:
                    dp[i] = True
                    break
    
    return dp[-1]

# Input array from standard input
arr = [int(x) for x in sys.stdin.readline().split()]

# Print the result to standard output
print(canJump(arr))
