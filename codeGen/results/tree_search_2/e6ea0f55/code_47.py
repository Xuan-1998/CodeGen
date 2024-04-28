def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = {(i, 0): nums[i] for i in range(n)}
    
    for i in range(n):
        for j in range(1, min(i+1, k)+1):
            if i-j >= 0:
                dp[(i, j)] = max(dp.get((i-j, j-1), (0, 0))[0] + nums[i], dp.get((i, j-1), (0, 0))[0])
    
    return max(sum(subsequence) for subsequence in dp.values())

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(maxSumSubsequence(nums, k))
