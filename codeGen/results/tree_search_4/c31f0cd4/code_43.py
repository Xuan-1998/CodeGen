from collections import defaultdict

def distinct_sums(subset):
    # Initialize a dictionary to store the sums
    dp = defaultdict(int)
    
    def dfs(i, s):
        if i == len(subset):
            return {s}
        res = set()
        for j in range(i, len(subset)):
            new_sum = s + subset[j]
            res.update(dfs(j+1, new_sum))
        return res
    
    # Calculate the sums and store them in dp
    for i in range(len(subset)):
        dfs(i, 0).update(dp)
    
    # Return the distinct sums
    return sorted(list({s for s in dp.values()}))

N = int(input())
subset = [int(x) for x in input().split()]
print(' '.join(map(str, distinct_sums(subset))))
