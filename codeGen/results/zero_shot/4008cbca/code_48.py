def solve():
    board = input().strip()
    hand = input().split()
    
    # Convert hand into sets for easy manipulation
    hand_sets = set([set([c]) if len(set([c])) == 1 else set([c]) for c in hand])
    
    min_insertions = float('inf')
    
    for i in range(len(board) + 1):
        for j in range(i + len(hand)):
            # Initialize sets for the current board and hand
            board_set = set()
            for k in range(i):
                board_set.add(board[k])
            for c in hand[j - i:j]:
                board_set.add(c)
            
            # Find the first group of consecutive balls with same color
            group_start = 0
            while group_start < len(board) and (board[group_start] not in board_set or board[group_start + 1] == board[group_start]):
                group_start += 2
            
            # Count the number of groups
            num_groups = 0
            current_group = group_start
            while current_group < len(board):
                if (current_group > group_start and board[current_group - 1] != board[current_group]) or (board[current_group] not in board_set):
                    num_groups += 1
                    group_start = current_group
                current_group += 2
            
            # Update the minimum number of insertions
            min_insertions = min(min_insertions, len(board) - i + j - i)
    
    return -1 if min_insertions == float('inf') else min_insertions
