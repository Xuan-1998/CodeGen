from collections import defaultdict

def min_moves(board, hand):
    memo = defaultdict(int)
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = 0
        for k in range(len(hand)):
            if hand[k] == board[i]:
                res += 1
                i += 1
                break
        
        if i < len(board):
            res += min(dp(i, j + 1), dp(i + 1, j) + 1)
        
        memo[(i, j)] = res
        return res
    
    return dp(0, 0)

board = input().strip()
hand = input().strip()

print(min_moves(board, hand))
