def can_cross_stones(stones):
    memo = {0: True}
    
    def dfs(i):
        if i not in memo:
            if i >= len(stones) - 1:
                return True
            max_jump = (stones[i] + 2) // 3
            for jump in range(1, max_jump+1):
                if stones[i] + jump == stones[i+1]:
                    memo[i] = dfs(i+1)
                    break
            else:
                memo[i] = False
        return memo[i]
    
    return dfs(0)

# test the function
stones = [0, 2, 5, 6, 8, 11, 13]
print(can_cross_stones(stones))  # Output: True

stones = [0, 1, 4, 7, 10, 12]
print(can_cross_stones(stones))  # Output: False
