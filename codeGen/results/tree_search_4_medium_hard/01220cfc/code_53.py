def canJump(nums):
    dp = [False] * len(nums)
    max_reachable = 0

    for i in range(len(nums)):
        if i > max_reachable:
            return False
        if i == len(nums) - 1:
            return True
        max_reachable = max(max_reachable, min(i + nums[i], len(nums) - 1))
    return False


if __name__ == "__main__":
    # Read input from stdin
    nums = list(map(int, input().split()))
    
    # Solve the problem and print the result to stdout
    if canJump(nums):
        print("Yes")
    else:
        print("No")
