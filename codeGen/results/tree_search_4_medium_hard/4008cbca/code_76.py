def min_insertions(board, hand):
    dp = {(i, set(h)) : float('inf') for i, h in enumerate(zip(board, hand))}
    
    dp[(0, hand)] = 0
    
    for i in range(len(board)):
        for j in range(min(i+1, len(hand)), -1, -1):
            if board[i] not in hand[:j]:
                dp[(i, set(hand[:j]))] = min(dp[(i-1, set(hand[:j]))) + 1
    
    res = dp.get((len(board), set()), -1)
    
    return res
