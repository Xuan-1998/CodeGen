def longest_subarray(nums):
    n = len(nums)
    dp = {0: 0}
    max_ones = 0

    for i, num in enumerate(nums):
        if num == 1:
            max_ones += 1
        else:
            max_ones = 0
        
        dp[i] = max(dp.get(i-1, 0), max_ones)
    
    return max(dp.values())

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))

if __name__ == "__main__":
    main()
