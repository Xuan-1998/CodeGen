def can_divide_sum(n, m, arr):
    # Initialize memoization dictionary
    memo = {}

    for num in arr:
        if num not in memo:  # Avoid redundant computations
            cumulative_sum = sum(arr[:arr.index(num) + 1])
            is_divisible = cumulative_sum % m == 0

            memo[num] = (cumulative_sum, is_divisible)

        # Check if the current cumulative sum is divisible by m
        if memo[num][1]:
            return 1  # Yes, there exists a subset with sum divisible by m

    return 0  # No such subset found

# Example usage:
n = int(input())  # number of elements in the set
m = int(input())  # value to check for divisibility
arr = [int(x) for x in input().split()]  # array of non-negative integers

print(can_divide_sum(n, m, arr))
