def find_sums(nums):
    memo = {}
    def dfs(i, s, n):
        if (i, s) in memo:
            return memo[(i, s)]
        
        sums = set()
        
        for j in range(i+1, len(nums)+1):
            sums.add(s + sum(nums[i:j]))
            
            if j < len(nums):
                res = dfs(j, s+nums[i], n)
                sums.update(res)
                
            memo[(i, s)] = sums
            
        return sums
    
    nums.sort()
    return ' '.join(map(str, sorted(set(dfs(0, 0, max(nums))))))

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    
    print(find_sums(nums))
