def distinct_sum_subsets(nums):
    memo = {}
    total_sum = sum(nums)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return [j]

        sums = []
        for num in nums[:i]:
            if j + num <= total_sum:
                new_sums = dp(i - 1, j + num)
                for s in new_sums:
                    if s not in sums:
                        sums.append(s)

        memo[(i, j)] = sums
        return sums

    subsets = []
    for i in range(len(nums) + 1):
        subsets.extend(dp(i, 0))

    unique_sums = sorted(list(set(subsets)))
    return ' '.join(map(str, unique_sums))

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(distinct_sum_subsets(nums))
