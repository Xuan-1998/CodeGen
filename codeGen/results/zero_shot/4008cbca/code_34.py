def insert_ball(board, hand):
    for ball in hand:
        if board == "" or (board[-1] != ball and board[-2] != ball):
            return board + ball
    return board

def remove_balls(board):
    while True:
        i = 0
        while i < len(board) - 2:
            if board[i] == board[i+1] == board[i+2]:
                return board[:i]
            i += 1
        break
    return board

def main():
    board = input()
    hand = input()

    result = float('inf')
    for ball in hand:
        new_board = insert_ball(board, [ball])
        while True:
            new_board = remove_balls(new_board)
            if not new_board:
                result = min(result, len(hand.split(','))
                break
    print(result if result != float('inf') else -1)

if __name__ == "__main__":
    main()
