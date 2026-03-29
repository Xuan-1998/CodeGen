n, k, z = map(int, input().split())
score = 0
moves_left = k

# Initialize the array
array = list(map(int, input().split()))

for _ in range(k):
    # Check if we have more than z consecutive left moves
    if moves_left > z:
        # If yes, try to make a right move
        for i in range(1, n):
            score += array[i]
            if i == n - 1 or array[i] <= array[i + 1]:
                break
        else:
            # If no right move is possible, backtrack and try to make left moves instead
            while moves_left > z:
                for i in range(n - 2, 0, -1):
                    if array[i] >= array[i - 1]:
                        score += array[i]
                        moves_left -= 1
                        break
    else:
        # If we have at most z consecutive left moves, try to make a left move
        for i in range(n - 2, 0, -1):
            if array[i] >= array[i - 1]:
                score += array[i]
                moves_left -= 1
                break

print(score)
