def totalDiamonds(N):
    # Initialize a 2D array dp where dp[i][j] represents the total number of diamonds in the first i rows and the first j columns.
    dp = [[0]*N for _ in range(N)]

    # Iterate through the grid from top to bottom and left to right, updating each cell based on its dependence on the previous cells.
    for i in range(1, N+1):
        for j in range(1, N+1):
            # Calculate the room number as the sum of its row and column numbers.
            roomNumber = i + j

            # Calculate the sum of even digits and odd digits in the current room number.
            evenSum = 0
            oddSum = 0
            numStr = str(roomNumber)
            for digit in numStr:
                if int(digit) % 2 == 0:
                    evenSum += int(digit)
                else:
                    oddSum += int(digit)

            # Calculate the total number of diamonds in the current room.
            dp[i-1][j-1] = abs(evenSum - oddSum)

    # Return the total number of diamonds in the entire grid.
    return sum([row[-1] for row in dp])

T = int(input())
for _ in range(T):
    N = int(input())
    print(totalDiamonds(N))
