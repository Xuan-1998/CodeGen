def count_creatures(heads_left, tails_left):
    dp = {(0, 0): 1}  # Base case: one combination with no heads or tails

    def recursive_count():
        if (heads_left, tails_left) in dp:
            return dp[(heads_left, tails_left)]
        
        result = 0
        for i in range(min(heads_left // 2 + 1, tails_left // 3 + 1)):
            if heads_left >= i * 2 and tails_left >= (i * 3):
                result += recursive_count()(heads_left - i * 2, tails_left - i * 3)
        
        dp[(heads_left, tails_left)] = result
        return result
    
    return recursive_count()()

# Read input from stdin
heads, tails = map(int, input().split())

# Calculate and print the number of possible combinations
result = count_creatures(heads, tails)
print(result if result > 0 else "No solutions")
