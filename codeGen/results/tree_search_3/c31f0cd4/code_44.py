def find_distinct_sums(nums):
    num_set = set()
    dp = {0: 1}
    distinct_sums = []

    for num in nums:
        temp_dp = {}
        for total in list(dp.keys()):
            dp[total + num] = dp.get(total + num, 0) + dp.get(total, 0)
            if total + num not in num_set:
                num_set.add(total + num)
                temp_dp[total + num] = dp[total + num]
        for key in list(temp_dp.keys()):
            del dp[key]
        dp.update(temp_dp)

    for key in sorted(list(dp.keys())):
        distinct_sums.append(str(key))

    return ' '.join(distinct_sums)


# Example usage:
N = int(input())
nums = [int(num) for num in input().split()]
print(find_distinct_sums(nums))
