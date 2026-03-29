from collections import deque

def canJump(nums):
    n = len(nums)
    memo = {(0, n-1): True}
    q = deque([(0, n-1)])

    while q:
        i, j = q.popleft()
        if i == j:
            return True

        for k in range(i+1, min(j+1, i+nums[i]+1)):
            memo[(k, j)] = True
            q.append((k, j))

    return False


# Testing the function with a sample array.
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(canJump(nums))
