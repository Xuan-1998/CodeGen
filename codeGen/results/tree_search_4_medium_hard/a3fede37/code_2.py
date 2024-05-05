def maxPathSum(val):
    if val < 0: return -1   # edge case: invalid tree structure

    memo = [[-1 for _ in range(2)] for _ in range(10**4 + 1)]

    def dp(val, parent):
        if memo[val][parent]: return memo[val][parent]   # memoized result
        if val < 0: return -1   # edge case: invalid tree structure

        leftSum = rightSum = -1
        if arr[2*val+1]:
            leftSum = dp(arr[2*val+1], val)
        if arr[2*val+2]:
            rightSum = dp(arr[2*val+2], val)

        maxSum = val + max(leftSum, rightSum)
        memo[val][parent] = max(maxSum, 0)   # ensure the result is non-negative

        return maxSum

    arr = list(map(int, input().split()))
    return dp(arr[1], -1)   # start from the root node
