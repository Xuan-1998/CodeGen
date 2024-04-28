def subset_sum_divisible(m, numbers):
    memo = {}
    for i in range(sum(numbers) + 1):
        memo[i] = False

    for num in numbers:
        for i in range(num - 1, sum(numbers) + 1):
            if memo[i]:
                memo[i + num] = True

    return any(memo[i] for i in range(0, m))

# Example usage
n = int(input())  # number of elements
m = int(input())  # value to check divisibility by
numbers = list(map(int, input().split()))  # array of n non-negative integers

print(subset_sum_divisible(m, numbers))
