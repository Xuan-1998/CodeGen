n = int(input().strip())
dp = [float('inf')] * 8
dp[0] = 0

for _ in range(n):
    price, vitamins = input().strip().split()
    price = int(price)
    mask = 0
    for vitamin in vitamins:
        if vitamin == 'A':
            mask |= 1
        elif vitamin == 'B':
            mask |= 2
        elif vitamin == 'C':
            mask |= 4
    
    # Update dp array with new combinations
    for i in range(8):
        dp[i | mask] = min(dp[i | mask], dp[i] + price)

# The answer is in dp[7], which represents all vitamins A, B, and C
answer = dp[7] if dp[7] != float('inf') else -1
print(answer)
