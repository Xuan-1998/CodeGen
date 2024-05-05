from collections import defaultdict

def solve():
    board = input()
    hand = input()

    # Count colors in hand
    hand_colors = defaultdict(int)
    for color in hand:
        if color in ['R', 'Y', 'B', 'G']:
            hand_colors[color] += 1

    # Initialize board colors and clusters
    board_colors = defaultdict(int)
    clusters = []
    prev_color = None
    cluster_start_index = -1
    for i, color in enumerate(board):
        if color == prev_color:
            continue
        if len(clusters) > 0 and clusters[-1][2] == i - 3:  # Consecutive same-colored balls
            clusters[-1].append(i)
        else:
            cluster_start_index = i
            clusters.append([i, i, i])
        prev_color = color

    # Count new balls needed to remove all clusters on the board
    total_new_balls = 0
    for cluster in clusters:
        if len(cluster) > 2:  # Cluster with three or more consecutive same-colored balls
            start_index = cluster[0]
            end_index = cluster[2]
            new_balls_needed = (end_index - start_index + 1) // 3 * hand_colors[cluster[0]]  # Calculate the number of new balls needed to remove all clusters on this board
            total_new_balls += new_balls_needed

    # Check if possible to remove all
    if total_new_balls > len(hand):
        print(-1)
    else:
        print(total_new_balls)

if __name__ == "__main__":
    solve()
