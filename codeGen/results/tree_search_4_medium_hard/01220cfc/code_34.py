def canJump(arr):
    memo = {0: True}
    for i in range(len(arr)):
        if i not in memo:
            memo[i] = arr[i] >= 1
        else:
            j = min(i+arr[i], len(arr)-1)
            while j >= 0 and (j not in memo or not memo[j]):
                j -= arr[j]
            memo[i] = j < 0
    return memo[-1]

# Example usage:
arr = [2,3,1,1,4]
print(canJump(arr)) # Output: True

arr = [3,2,1,0,4]
print(canJump(arr)) # Output: False
