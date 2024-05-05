def solve():
    board = input()
    hand = input()

    # Step 1: Sort the hand balls
    hand_sorted = sorted(hand)

    # Step 2: Initialize a variable to store the minimum number of insertions needed
    min_insertions = float('inf')

    # Step 3: Iterate over the possible positions where we can insert the first ball from the hand
    for i in range(len(board) + 1):
        # Step 4: Insert the first ball at this position and update the board string
        updated_board = board[:i] + hand_sorted[0] + board[i:]

        # Step 5: Initialize a variable to store the number of insertions needed for the remaining part of the board
        remaining_insertions = 0

        # Step 6: Check if there are three or more balls of the same color touching in the updated board
        for j in range(len(updated_board) - 2):
            if updated_board[j] == updated_board[j+1] == updated_board[j+2]:
                break
        else:
            # If no such group is found, continue with the rest of the board
            remaining_insertions = len(updated_board) - (j + 3)

        # Step 7: Calculate the total number of insertions needed for this position
        total_insertions = i + remaining_insertions

        # Step 8: Update the minimum number of insertions if this position gives a better solution
        min_insertions = min(min_insertions, total_insertions)

    # Step 9: Check if it is possible to remove all the balls
    if min_insertions == float('inf'):
        print(-1)
    else:
        print(min_insertions)

if __name__ == "__main__":
    solve()
