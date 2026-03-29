def max_score(arr):
    n, k, z = len(arr), k, z
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j > 0 and i - j > z:
            res = dp(i-1, z)
        elif j == 0:
            res = arr[i]
        else:
            left = dp(i-1, j-1) + arr[i]
            right = dp(i+1, j-1) + arr[i-1]
            res = max(left, right)

        memo[(i, j)] = res
        return res

    return dp(1, k)
