def min_moves_to_remove_boards(board, hand):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(board) or j == len(hand):
            return 0
        
        res = float('inf')
        
        for k in range(j + 1):
            new_board = board[:i] + list(hand[k])
            new_hand = hand[k+1:]
            
            if can_remove(new_board):
                res = min(res, helper(i + len(new_hand), new_hand))
                
            if res == float('inf'):
                return -1
        
        memo[(i, j)] = res
        return res
    
    def can_remove(board):
        for i in range(len(board) - 2):
            if board[i] == board[i+1] == board[i+2]:
                return True
        
        return False
    
    return helper(0, len(hand))

board = input().strip()
hand = input().strip()

print(min_moves_to_remove_boards(list(board), list(hand)))
