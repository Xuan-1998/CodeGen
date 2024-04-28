def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == total_sum - num:
            return i
        left_sum += num
    return -1

if __name__ == "__main__":
    nums = [list(map(int, input().split())) for _ in range(int(input()))]
    print(pivotIndex(nums[0]))
