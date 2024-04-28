def max_points(n, a):
    memo = {}

    def dp(sum_, fully_used):
        if (sum_, fully_used) in memo:
            return memo[(sum_, fully_used)]

        if fully_used:
            return 0

        if sum_ == 0:
            return 0

        delete_points = 1 + dp(-a[0], True)
        keep_points = dp(sum_, fully_used)

        result = max(delete_points, keep_points)
        memo[(sum_, fully_used)] = result
        return result

    return dp(0, False)
