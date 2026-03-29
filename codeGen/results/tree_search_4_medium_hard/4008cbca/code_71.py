===BEGIN SOLUTION===
from collections import deque
hand_colors = set(input().strip())
board = input().strip()

dp = {0: 0}
queue = deque([(0, 0)])  # (position, min_moves)

while queue:
    pos, min_moves = queue.popleft()
    if dp.get(pos):
        continue

    for color in hand_colors:
        hand_count = board.count(color)
        new_board = board[:pos] + hand_count * color
        removeable = False
        for i in range(1, len(new_board)):
            if new_board[i-1] == new_board[i]:
                for j in range(i):
                    while new_board[j:j+3].count(new_board[i]) >= 3:
                        new_board = new_board[:j] + 'R'*(new_board[i-1]=='R') + new_board[j+3:]
                        removeable = True
                        break
                if removeable:
                    break

        if not removeable:
            continue
        new_min_moves = min_moves + hand_count
        queue.append((pos+len(new_board), new_min_moves))
        dp[pos+len(new_board)] = new_min_moves

print(-1) if pos+len(board) not in dp else print(dp[pos+len(board)])
