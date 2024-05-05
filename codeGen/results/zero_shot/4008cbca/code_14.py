def min_balls_to_insert():
    board = input().strip()
    hand = input().strip()

    remaining_hand = set(hand)
    removed = 0

    for i in range(len(board)):
        if board[i] == 'R' and (i == 0 or board[i-1] != 'R') and (i == len(board)-1 or board[i+1] != 'R'):
            removed += 3
            remaining_hand -= {'R'}
        elif board[i] in hand:
            remaining_hand -= {board[i]}
    if any(c in remaining_hand for c in ['R', 'Y', 'B', 'G', 'W']):
        print(-1)
    else:
        print(len(remaining_hand))

min_balls_to_insert()
