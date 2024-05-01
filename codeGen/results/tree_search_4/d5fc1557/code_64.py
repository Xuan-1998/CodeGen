def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(n):
        if nums[i] == 1:
            dp[i+1] = max(dp[i], dp[i-1]) + 1 if i > 0 else 1
        else:
            dp[i+1] = dp[i]

    return max(dp) - 1

def find_longest_subarray(nums):
    n = len(nums)
    
    # Handle the case where there's no 1's in the array.
    longest = 0
    
    for i, num in enumerate(nums):
        if num == 1:
            # Start a new subarray when we see a 1
            dp = [0]
            for j in range(i, n):
                if nums[j] == 1:
                    dp.append(dp[-1] + 1)
                else:
                    dp.append(0)
            longest = max(longest, max(dp))
        else:
            # If all elements are 0's, return 0
            return 0
    
    return longest - 1

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    print(find_longest_subarray(nums))

if __name__ == "__main__":
    main()
