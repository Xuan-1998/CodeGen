from collections import deque

def min_moves_to_remove_all_boards(board, hand):
    # Create a dictionary to store the DP table
    dp = {(board, i): float('inf') for i in range(len(hand) + 1)}
    
    # Base case: when there are no more balls in hand
    dp[(board, 0)] = 0
    
    # Perform BFS from each possible board state
    queue = deque([(board, 0)])
    while queue:
        (cur_board, cur_hand) = queue.popleft()
        
        # Iterate over the possible moves (inserting a ball)
        for i in range(len(cur_board)):
            new_board = cur_board[:i] + hand[0] + cur_board[i:]
            
            # Calculate the number of moves needed to remove all balls
            if len(new_board) > 1 and ''.join([cur_board[i-1], cur_board[i], cur_board[i+1]]) in ['RRR', 'YYY', 'BBB', 'GGG']:
                moves = dp[(new_board, cur_hand - 1)] + 1
            else:
                moves = dp[(new_board, cur_hand - 1)] + 1 if cur_hand > 0 else float('inf')
            
            # Update the DP table if a better solution is found
            if moves < dp[(new_board, cur_hand)]:
                dp[(new_board, cur_hand)] = moves
                
        # Add all possible next states to the queue
        for i in range(len(cur_board)):
            new_board = cur_board[:i] + hand[0] + cur_board[i:]
            
            if len(new_board) > 1 and ''.join([cur_board[i-1], cur_board[i], cur_board[i+1]]) in ['RRR', 'YYY', 'BBB', 'GGG']:
                queue.append((new_board, cur_hand - 1))
            else:
                queue.append((new_board, cur_hand - 1 if cur_hand > 0 else -1))
    
    # Return the minimum number of moves needed to remove all balls
    return dp[(board, len(hand))] if dp[(board, len(hand))] != float('inf') else -1

# Example usage:
if __name__ == "__main__":
    board = input()
    hand = list(input())
    print(min_moves_to_remove_all_boards(board, hand))
