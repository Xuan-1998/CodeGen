import sys

def find_winner(M, X):
    dp = [0] * (X + 1)
    
    # Base case: For 1 player, the winner is always 1.
    dp[1] = 1
    
    for i in range(2, X + 1):
        # Calculate the previous winner by considering how many times the coin has been passed.
        prev_winner = (i - 1) % M + 1
        if i < M:
            # For small values of i, we can handle this manually to avoid unnecessary calculations.
            dp[i] = prev_winner
        else:
            # Calculate the winner by considering the previous winner and how many times the coin has been passed.
            dp[i] = prev_winner + (i - 1) // M
    
    return dp

T = int(input())
for _ in range(T):
    M, X = map(int, input().split())
    winners = find_winner(M, X)
    print(*winners[1:], sep='\n')
