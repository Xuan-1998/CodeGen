===BEGIN CODE===
def find_sums(set):
    n = len(set)
    dp = [[[] for _ in range(n+1)] for _ in range(n+1)]
    
    def helper(i, sum, subset):
        if i == n:
            return [sum]
        
        results = []
        for j in range(i, n):
            if set[j] > set[i]:
                break
            new_sum = sum + set[j]
            new_subset = subset + [set[j]]
            
            if not dp[j][j+1]:  # Memoization
                dp[j][j+1] = helper(j+1, new_sum, new_subset)
            
            results += dp[j][j+1]
        
        return results
    
    for i in range(n):
        for j in range(i, n):
            if set[i] > set[j]:
                break
            dp[i][j+1] = helper(i, 0, [])
    
    sums = []
    seen = set()
    
    for i in range(n):
        for j in range(i, n):
            if set[i] > set[j]:
                break
            for result in dp[i][j+1]:
                new_sum = sum(result)
                if new_sum not in seen:
                    seen.add(new_sum)
                    sums.append(str(new_sum))
    
    return " ".join(sums)

n = int(input())
set = list(map(int, input().split()))
print(find_sums(set))

===END CODE===
