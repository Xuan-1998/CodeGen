def subset_sums(nums):
    memo = {}
    result = []

    def recursive_subset_sum(i, total, size):
        if (i, total) in memo:
            return memo[(i, total)]

        if i >= len(nums):
            memo[(i, total)] = [total]
            return [total]

        included = recursive_subset_sum(i + 1, total + nums[i], size + 1)
        excluded = recursive_subset_sum(i + 1, total, size)

        sums = set(included + excluded)
        memo[(i, total)] = sorted(list(sums))
        return memo[(i, total)]

    for i in range(len(nums)):
        result.extend(recursive_subset_sum(0, 0, 0))

    unique_sums = set()
    for subset in result:
        for sum_val in subset:
            if sum_val not in unique_sums:
                unique_sums.add(sum_val)

    return ' '.join(map(str, sorted(list(unique_sums))))


if __name__ == '__main__':
    N = int(input())
    nums = [int(x) for x in input().split()]
    print(subset_sums(nums))
