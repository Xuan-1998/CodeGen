n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
dp = set()

def dfs(i, sum):
    if i == n:
        dp.add(sum)
        return
    dfs(i+1, sum)
    dfs(i+1, sum + nums[i])

dfs(0, 0)
