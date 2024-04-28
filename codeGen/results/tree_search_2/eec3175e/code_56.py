def find_subset_sum_divisible_by_m(n, m, numbers):
    dp = [[False] * (m + 1) for _ in range(sum(numbers) + 1)]

    for total_sum in range(1, sum(numbers) + 1):
        if total_sum % m == 0:
            dp[total_sum][0] = True

    for number in numbers:
        for total_sum in range(sum(numbers), number - 1, -1):
            if total_sum >= number and (dp[total_sum - number][number % m]):
                dp[total_sum][number % m] = True

    return any(dp[-1])

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
print(find_subset_sum_divisible_by_m(n, m, numbers))
