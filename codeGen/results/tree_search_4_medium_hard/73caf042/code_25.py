import sys

def calculate_diamonds(N):
    # Initialize a 2D array dp with all elements set to 0.
    dp = [[0] * N for _ in range(N)]

    # Calculate the number of diamonds in each room using memoization.
    def f(i, j):
        if i > j:
            return 0
        if dp[i][j]:
            return dp[i][j]
        
        # Calculate the sum of even digits and odd digits in the current room number.
        room_number = (i + j)
        even_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 == 0)
        odd_sum = sum(int(digit) for digit in str(room_number) if int(digit) % 2 != 0)
        diamonds = abs(even_sum - odd_sum)

        # Store the value in dp array.
        dp[i][j] = diamonds + f(i-1, j-1) if i > 1 and j > 1 else 0
        return dp[i][j]

    # Calculate the total number of diamonds in the grid.
    total_diamonds = sum(sum(1 for _ in row) for row in dp)
    print(total_diamonds)

T = int(input())
for _ in range(T):
    N = int(input())
    calculate_diamonds(N)
