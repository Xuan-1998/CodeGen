from collections import defaultdict

def find_distinct_sums(sets):
    memo = defaultdict(int)
    result = set()

    def dfs(subset, current_sum):
        if current_sum in memo:
            return
        memo[current_sum] = 1
        
        if len(subset) == 0:
            result.add(current_sum)
        else:
            for i in range(len(subset)):
                dfs(subset[:i] + subset[i+1:], current_sum + subset[0])
    
    for s in sets:
        dfs(s, 0)

    return sorted(list(result))

# Example usage
sets = [[1, 2], [3, 4], [5]]
print(find_distinct_sums(sets))
