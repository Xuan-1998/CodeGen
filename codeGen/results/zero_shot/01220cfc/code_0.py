def can_jump(nums):
    n = len(nums)
    last_pos = n - 1

    for i in range(n - 1, -1, -1):
        if i + nums[i] >= last_pos:
            return True
        last_pos = i

    return False

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(can_jump(nums))
