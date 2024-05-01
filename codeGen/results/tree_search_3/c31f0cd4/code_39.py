from collections import defaultdict

def find_distinct_sums():
    N = int(input())
    nums = list(map(int, input().split()))
    
    memo = defaultdict(int)
    sums = set()
    
    def dfs(current_sum, start):
        if current_sum in memo:
            return
        for i in range(start, N):
            new_sum = current_sum + nums[i]
            if new_sum not in memo:
                memo[new_sum] = 1
                dfs(new_sum, i+1)
        sums.add(current_sum)
    
    dfs(0, 0)
    
    print(' '.join(map(str, sorted(list(sums)))))

find_distinct_sums()
