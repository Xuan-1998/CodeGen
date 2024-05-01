def max_points_to_earn(n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Base cases: dp[0][k] = 0 for all k, and dp[i][i] = i for all i
    for i in range(n+1):
        dp[i][i] = i

    # Fill in the table row by row or column by column
    for len_subsequence in range(2, n+1):
        for left_index in range(n - len_subsequence + 1):
            right_index = left_index + len_subsequence - 1
            max_points_to_earn_without_current_element = dp[left_index][right_index]
            if left_index < right_index:
                max_points_to_earn_by_deleting_current_element = dp[left_index+1][right_index-1] + len_subsequence
                dp[left_index][right_index] = max(max_points_to_earn_without_current_element, max_points_to_earn_by_deleting_current_element)

    return dp[0][n]
