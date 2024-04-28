def has_divisible_subset(n, m, arr):
    # Initialize memoization table with all subsets having sums from 0 to (sum of all elements)
    memo = [False] * (sum(arr) + 1)

    # Compute sum of each subset and store it in the memoization table
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total % m == 0:
                return 1  # Found a divisible subset!
            memo[total] = True

    return 0  # No divisible subset found

# Example usage:
n = int(input())  # Number of elements in the set
m = int(input())  # Value to check for divisibility
arr = list(map(int, input().split()))  # Array of non-negative integers

print(has_divisible_subset(n, m, arr))
