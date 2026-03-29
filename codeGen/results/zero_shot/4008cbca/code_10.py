import collections

def solve(board, hand):
    # Create a dictionary to store the graph nodes
    graph = {}

    # Define the initial node (the initial state)
    initial_node = {"board": board, "hand": hand}
    graph[0] = [initial_node]

    # Define the goal node (no balls left on the board)
    goal_node = {"board": "", "hand": ""}
    graph[-1] = [goal_node]

    # Create a queue for BFS
    queue = collections.deque([(0, 0)])  # (node_id, distance)

    while queue:
        node_id, distance = queue.popleft()
        if node_id == -1:
            return distance

        node = graph[node_id][0]
        board = node["board"]
        hand = node["hand"]

        for i in range(len(board)):
            # Try inserting a ball at each position
            for c in "RYBGW":
                new_board = list(board)
                new_hand = hand.replace(c, "")
                if len(new_hand) < 5 and all([c not in new_board[i-1:i+2] or len(set(new_board[i-1:i+2])) > 1 for i in range(len(new_board))]):
                    # Create a new node representing the updated state
                    new_node = {"board": "".join(new_board), "hand": new_hand}
                    graph[len(graph)] = [new_node]
                    queue.append((len(graph), distance + 1))

    return -1

# Example usage:
board = input()
hand = input()
print(solve(board, hand))
