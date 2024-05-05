import sys

def read_input():
    return [int(num) for num in sys.stdin.readline().split()]

def find_longest_increasing_subsequence(nums):
    dp = [0] * max(nums)
    for num in nums:
        i = 0
        while i < len(dp) and dp[i] < num:
            i += 1
        dp[i] = num
    return len(dp)

if __name__ == "__main__":
    nums = read_input()
    print(find_longest_increasing_subsequence(nums))
