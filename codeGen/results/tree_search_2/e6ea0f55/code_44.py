import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    memo = {(i, 0): (nums[0], 0) for i in range(n)}

    def dp(i):
        if (i, 0) not in memo:
            j = max(0, i-k)
            memo[(i, 0)] = max((memo[j][0] + nums[i], i) if j > 0 else (0, i), key=lambda x: x[0])
        return memo[(i, 0)]

    return max(dp(i)[0] for i in range(n))

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(max_sum_subsequence(nums, k))

if __name__ == "__main__":
    main()
