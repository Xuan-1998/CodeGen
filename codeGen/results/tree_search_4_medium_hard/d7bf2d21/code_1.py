def find_number_of_longest_increasing_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    memo = {i: 0 for i in range(n)}
    
    def dfs(i):
        if memo[i] > 0:
            return memo[i]
        
        max_len = 1
        for j in range(i):
            if arr[j] < arr[i]:
                max_len = max(max_len, dfs(j) + 1)
        memo[i] = max_len
        return max_len
    
    longest_lengths = [dfs(i) for i in range(n)]
    
    return sum(1 for x in set(longest_lengths) if longest_lengths.count(x) == 1)

print(find_number_of_longest_increasing_subsequences())
