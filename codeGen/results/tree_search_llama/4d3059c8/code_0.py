def pivotIndex(nums):
    n = len(nums)
    total_sum = sum(nums)

    left_sum = 0
    cumulative_sums = {0: -1}

    for i, num in enumerate(nums):
        right_sum = total_sum - num - left_sum
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(pivotIndex(nums))
