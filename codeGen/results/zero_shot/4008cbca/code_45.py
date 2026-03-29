def can_remove_all_balls(board, hand):
    while True:
        # Check if there are three or more consecutive balls of the same color in the board.
        i = 0
        while i < len(board) - 2:
            if board[i] == board[i+1] == board[i+2]:
                return False
            i += 1
        
        # If no such sequence is found, check if all balls can be removed by inserting from the hand.
        for c in set(hand):
            count = hand.count(c)
            j = 0
            while j < len(board) - 2:
                k = j
                while k < len(board) and board[k] == board[k+1] == board[k+2]:
                    k += 3
                if k > j:
                    new_board = list(board[:j]) + [c] * (k-j)
                    if can_remove_all_balls(''.join(new_board), hand):
                        return True
                j += 1
        
        # If no such sequence is found and all balls cannot be removed, then it's not possible to remove all the balls.
        return False

def min_insertions_needed(board, hand):
    result = -1
    for _ in range(len(hand)):
        if can_remove_all_balls(board, hand):
            return _
        else:
            board += hand[0]
            hand = hand[1:]
    return result

if __name__ == "__main__":
    board = input()
    hand = list(input())
    
    print(min_insertions_needed(board, hand))
