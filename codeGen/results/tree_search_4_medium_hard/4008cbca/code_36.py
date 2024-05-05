from collections import defaultdict

def dp(board, hand, memo={}):
    if (board, hand) in memo:
        return memo[(board, hand)]

    n = len(board)
    hand_set = set(hand)

    # Base case: If the board is empty, we don't need to do anything.
    if not board:
        return 0

    # Initialize minimum moves
    min_moves = float('inf')

    for i in range(n):
        if board[i] in hand_set:
            # If the current ball is in our hand, remove it and consider the remaining board.
            new_board = board[:i] + board[i+1:]
            new_hand = hand.replace(board[i], '', 1)
            min_moves = min(min_moves, 1 + dp(new_board, new_hand))

    memo[(board, hand)] = min_moves
    return min_moves

def main():
    board = input().strip()
    hand = input().strip()

    # Convert inputs to sets for faster lookups
    board_set = set(board)
    hand_set = set(hand)

    # Calculate the minimum number of moves needed
    min_moves = dp(board, hand)

    if min_moves == float('inf'):
        print(-1)  # Not possible to remove all balls.
    else:
        print(min_moves)

if __name__ == '__main__':
    main()
