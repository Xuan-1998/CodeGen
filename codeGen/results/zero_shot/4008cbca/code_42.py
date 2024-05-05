board = input()
hand = input()
total_operations = 0

for i in range(len(board)):
    consecutive_count = 0
    for j in range(i, len(board)):
        if board[j] == board[i]:
            consecutive_count += 1
        else:
            break
    if consecutive_count >= 3:
        total_operations += consecutive_count - 2

print(total_operations)
