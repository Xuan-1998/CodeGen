import sys

def longest_increasing_subsequences(nums):
    n = len(nums)
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i):
            if nums[j] < nums[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
    
    return max(max(row) for row in dp)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(longest_increasing_subsequences(nums))

if __name__ == "__main__":
    main()
