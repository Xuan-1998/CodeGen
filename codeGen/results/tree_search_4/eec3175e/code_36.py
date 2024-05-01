def can_sum_divisible_by_m(nums, m):
    n = len(nums)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    memo = {(i, k): False for i in range(n + 1) for k in range(m + 1)}
    
    def dfs(i, k):
        if memo[(i, k)]:
            return memo[(i, k)]
        
        if k == 0:
            return True
        
        if i == 0:
            return False
        
        x = nums[i - 1]
        if k >= x and (k % m) == (x % m):
            return dfs(i - 1, (k + x) % m) or dfs(i - 1, k)
        
        memo[(i, k)] = dfs(i - 1, k)
        return memo[(i, k)]
    
    return dfs(n, 0)

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    result = can_sum_divisible_by_m(nums, m)
    
    print(result)

if __name__ == "__main__":
    main()
