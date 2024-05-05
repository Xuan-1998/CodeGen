import sys

def check_consecutive(board):
    for i in range(len(board) - 2):
        if board[i] == board[i+1] == board[i+2]:
            return True
    return False

def remove_consecutive(board):
    while True:
        found = False
        new_board = ''
        for char in board:
            if not found and (char != board[-1] or len(new_board) < 3):
                new_board += char
            else:
                found = True
                if char == board[-1]:
                    break
        board = new_board
        if not found:
            break
    return board

def main():
    board = sys.stdin.readline().strip()
    hand = sys.stdin.readline().strip()
    
    # Initialize the number of balls to insert
    num_insertions = 0
    
    while True:
        # Check if it's possible to remove all the balls
        if check_consecutive(board):
            break
        
        # Remove consecutive same-colored balls
        board = remove_consecutive(board)
        
        # Increment the number of balls inserted
        num_insertions += len(hand) - (len(set(hand)) - 1)
    
    # If no more removals are possible, it's not possible to remove all the balls
    if check_consecutive(board):
        print(-1)
    else:
        print(num_insertions)

if __name__ == "__main__":
    main()
