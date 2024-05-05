from collections import defaultdict

def min_moves_to_remove_all_balls():
    board = input().strip()
    hand = list(input().strip())

    memo = defaultdict(int)

    def dfs(i, prev_color):
        if i >= len(board):
            return 0
        if (i, prev_color) in memo:
            return memo[(i, prev_color)]
        
        remove_left = dfs(i - 1, board[i]) if i > 0 else float('inf')
        insert_new = dfs(i + 1, 'W') if hand[0] == 'R' and len(hand) > 1 else float('inf')

        if (board[i-3:i+1].count(board[i])) >= 3:
            return -1
        else:
            return min(remove_left, insert_new)

    print(dfs(0, 'W'))

if __name__ == "__main__":
    min_moves_to_remove_all_balls()
