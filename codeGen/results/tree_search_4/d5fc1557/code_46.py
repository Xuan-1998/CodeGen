from collections import defaultdict

def longest_subarray(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        max_length = 0
        count = 0
        temp_count = defaultdict(int)
        
        for j in range(i, -1, -1):
            if nums[j] == 1:
                count += 1
                temp_count[1] += 1
            else:
                if not temp_count:
                    break
                
                while temp_count[1]:
                    temp_count[1] -= 1
                    count -= 1
                    
            max_length = max(max_length, count)
        
        for j in range(i + 1, n):
            if nums[j] == 1:
                count += 1
                temp_count[1] += 1
            else:
                if not temp_count:
                    break
                
                while temp_count[1]:
                    temp_count[1] -= 1
                    count -= 1
                    
            dp[i][j] = max(dp[i][j-1], count)
    
    return max(max(row) for row in dp) - 1

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))

if __name__ == "__main__":
    main()
