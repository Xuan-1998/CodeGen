===BEGIN CODE===
def reachable(arr):
    n = len(arr)
    memo = {i: False for i in range(n)}
    def helper(i):
        if memo[i]:
            return memo[i]
        if i == n - 1:
            memo[i] = True
            return memo[i]
        if arr[i] == 0 or i + arr[i] >= n:
            memo[i] = False
            return memo[i]
        for j in range(i + 1, min(i + arr[i] + 1, n)):
            if not helper(j):
                break
        else:
            memo[i] = True
        return memo[i]

    return helper(0)
