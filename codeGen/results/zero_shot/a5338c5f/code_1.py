from collections import deque

def min_seconds_to_eat_candies(n, s, k, candies, colors):
    # Initialize the DP table with infinities
    dp = [[[float('inf')] * (k+1) for _ in range(4)] for _ in range(n+1)]
    dp[s][3][0] = 0  # Starting state (position s, no last color, 0 candies eaten)
    color_map = {'R': 0, 'G': 1, 'B': 2}
    queue = deque([(s, 3, 0)])  # Use a queue to perform BFS

    while queue:
        pos, last_color, eaten = queue.popleft()
        current_time = dp[pos][last_color][eaten]
        # Try to eat candies from the current box if the color is different
        if last_color != color_map[colors[pos-1]] and eaten < k:
            new_eaten = min(eaten + candies[pos-1], k)
            if dp[pos][color_map[colors[pos-1]]][new_eaten] > current_time:
                dp[pos][color_map[colors[pos-1]]][new_eaten] = current_time
                queue.append((pos, color_map[colors[pos-1]], new_eaten))
        # Try to move to the next or previous box
        for new_pos in [pos-1, pos+1]:
            if 1 <= new_pos <= n and candies[new_pos-1] > candies[pos-1]:
                if dp[new_pos][last_color][eaten] > current_time + 1:
                    dp[new_pos][last_color][eaten] = current_time + 1
                    queue.append((new_pos, last_color, eaten))

    # Find the minimum time to eat at least k candies
    min_time = min(min(dp[i][j][k] for j in range(4)) for i in range(1, n+1))
    return -1 if min_time == float('inf') else min_time

# Read input from stdin
n, s, k = map(int, input().split())
candies = list(map(int, input().split()))
colors = input().split()

# Print the result to stdout
print(min_seconds_to_eat_candies(n, s, k, candies, colors))
