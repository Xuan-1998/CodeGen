from collections import defaultdict

def max_points(n, a):
    # Create a memoized dictionary to store subproblem results
    dp = defaultdict(int)

    def memoized_delete(i):
        if i < 0:
            return 0
        if i >= n:
            return 0
        if dp[i] > 0:
            return dp[i]

        # Compute the maximum number of points for this subsequence
        max_points_here = 1
        last_deleted = a[i]
        for j in range(i - 1, -1, -1):
            if a[j] == last_deleted + 1 or a[j] == last_deleted - 1:
                max_points_here += memoized_delete(j - 1)
                break
        dp[i] = max_points_here

        return max_points_here

    # Main function to find the maximum number of points
    def delete_max_points():
        max_points_earned = 0
        for i in range(n):
            max_points_earned += memoized_delete(i)
        return max_points_earned

    n, *a = [int(x) for x in input().split()]
    print(delete_max_points())
