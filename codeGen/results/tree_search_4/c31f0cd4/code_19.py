def subsetSums(nums):
    n = len(nums)
    memo = {}
    
    def dfs(i, total):
        if (i, total) in memo:
            return memo[(i, total)]
        
        if i == n:
            return [total]
        
        include = dfs(i+1, total + nums[i])
        exclude = dfs(i+1, total)
        
        result = set(include)
        result.update(exclude)
        
        memo[(i, total)] = result
        return list(result)
    
    sums = set()
    for i in range(n):
        for total in dfs(i, 0):
            sums.add(total)
    
    return sorted(list(sums))

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    print(' '.join(map(str, subsetSums(nums))))

if __name__ == "__main__":
    main()
