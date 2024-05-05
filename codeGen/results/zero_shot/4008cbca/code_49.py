board = input()
hand = input()

board_state = [c for c in board]

def is_possible_to_remove_all(board_state):
    for i in range(len(board_state) - 2):
        if board_state[i] == board_state[i+1] == board_state[i+2]:
            return False
    return True

def min_insertions_to_remove_all(board_state, hand):
    insertions = 0
    while not is_possible_to_remove_all(board_state) and hand:
        next_ball = hand[0]
        for i in range(len(board_state)):
            if board_state[i] != next_ball:
                board_state.insert(i, next_ball)
                break
        hand = hand[1:]
        insertions += 1
    return insertions if is_possible_to_remove_all(board_state) else -1

print(min_insertions_to_remove_all(board_state, hand))
