def find_sums(nums):
    n = len(nums)
    dp = {}
    
    for mask in range(1 << n):  # 2^n
        subset_sum = 0
        for i in range(n):
            if (mask & (1 << i)):  # Check the ith bit of the mask
                subset_sum += nums[i]
        
        if subset_sum not in dp:
            dp[subset_sum] = True
        
        for prev_mask in range(1 << n):  
            if prev_mask & (1 << i):
                prev_subset_sum = 0
                for j in range(n):
                    if prev_mask & (1 << j):
                        prev_subset_sum += nums[j]
                
                if subset_sum + prev_subset_sum not in dp:
                    dp[subset_sum + prev_subset_sum] = True
        
    return sorted(list(dp.keys()))

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    
    print(' '.join(map(str, find_sums(nums))))

if __name__ == "__main__":
    main()
