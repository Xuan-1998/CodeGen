def find_subset_sum_divisible_by_m(n, m, arr):
    # Create a memo array to store results of subproblems
    memo = [[False] * (m + 1) for _ in range(n + 1)]

    def dp(i, s):
        # Base case: When n = 1, return True if arr[0] is less than m
        if i == 1:
            return s < m

        # If the result is already stored in memo, return it
        if memo[i][s]:
            return True

        # Recursive case: For each subset of size i, consider including or excluding the current element
        for j in range(i):
            if dp(j, s) and (not arr[j] or s + arr[j] <= m):
                # If the sum is divisible by m, mark it as True in memo
                if (s + arr[j]) % m == 0:
                    memo[i][s] = True
                    return True

        # Store the result of this subproblem in memo
        memo[i][s] = False

    # Start from the base case with n = 1 and an empty subset sum
    for i in range(n + 1):
        if dp(i, 0):
            return 1

    return 0

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(find_subset_sum_divisible_by_m(n, m, arr))
