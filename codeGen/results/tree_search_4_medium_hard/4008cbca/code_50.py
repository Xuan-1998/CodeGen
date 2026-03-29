def min_balls_to_remove():
    board = input()
    hand = input()

    stack = []
    for ball in board:
        stack.append(ball)

    removed_count = 0
    while True:
        same_color_count = 1
        color = stack[-1]
        for i in range(len(stack) - 2, -1, -1):
            if stack[i] == color:
                same_color_count += 1
            else:
                break
        if same_color_count >= 3:
            removed_count += same_color_count - 2
            while same_color_count > 2:
                stack.pop()
                same_color_count -= 1
        else:
            break

    return len(board) - removed_count


print(min_balls_to_remove())
