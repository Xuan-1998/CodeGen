def total_diamonds(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    room_count = {}

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1:
                # Base case: calculate diamonds directly
                dp[i][j] = abs(sum(int(digit) for digit in str(i * (i + j - 1))) // 2)
            else:
                # Recursively calculate diamonds from the previous room and the current room
                prev_room = i - 1, j - 1
                if prev_room not in room_count:
                    room_count[prev_room] = dp[prev_room[0]][prev_room[1]]
                dp[i][j] = dp[prev_room[0]][prev_room[1]] + abs(sum(int(digit) for digit in str(i * (i + j - 1))) // 2)

    total_diamonds = sum(dp[i][j] for i in range(1, n + 1) for j in range(1, n + 1))
    return total_diamonds
