code
if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    print(maxSumSubsequence(nums, k))
