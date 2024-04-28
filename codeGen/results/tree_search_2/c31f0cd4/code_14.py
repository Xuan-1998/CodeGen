def find_sums():
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    dp = [[set()] for _ in range(n+1)]
    dp[0][0] = {0}
    
    for i in range(1, n+1):
        for j in range(i+1):
            for k in dp[i-1][j-k]:
                dp[i].append(dp[i-1][j-k].copy())
                dp[i][-1].add(k + nums[i-1])
                
    return ' '.join(map(str, sorted({sum(s) for s in [set()]+[list(subset) for subset in dp[-1]]})))

print(find_sums())
