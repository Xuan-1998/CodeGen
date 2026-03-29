def can_cross(stones):
    dp = {(i, 0): True for i in range(len(stones))}
    
    def helper(i, d):
        if (i, d) not in dp:
            dp[(i, d)] = any(
                abs(stones[i] - stones[j]) <= d + k and dp.get((j, k), False)
                for k in range(1, 3) if j >= i-k
            )
        return dp[(i, d)]
    
    result = helper(len(stones)-1, 0)
    return result

# Read input from stdin
stones = [int(x) for x in input().split()]

print(can_cross(stones))
