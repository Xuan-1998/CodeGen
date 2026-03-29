from sys import stdin

def canJump(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums)):
        if i > lastPos:
            return False
        lastPos = max(lastPos, i + nums[i])
    return True

# Read input from standard input.
inputArray = [int(i) for i in stdin.readline().split()]

if canJump(inputArray):
    print(True)
else:
    print(False)
