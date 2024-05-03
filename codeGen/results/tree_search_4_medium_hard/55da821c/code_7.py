from collections import defaultdict

def min_replanted_plants(n, m):
    # Initialize the memoization dictionary
    dp = defaultdict(int)

    for i in range(1, n+1):
        s_i, x_i = [int(), float()]  # Get the species and position of the ith plant
        current_section = s_i // (m + 1)  # Calculate the current section

        if i == 1:
            # For the first plant, just increment the replanted plants count
            dp[(0, 0)] += 1
        else:
            # Get the previous state from the memoization dictionary
            prev_state = dp.keys().index((dp[(current_section-1, 0)], current_section-1))

            # Calculate the new state by incrementing the replanted plants count and updating the section
            new_state = (prev_state[0] + 1, current_section)
            dp[new_state] = min(dp.get(new_state, float('inf')), prev_state[0] + 1)

    return max(0, max(dp.values()) - 1)  # Return the minimum number of replanted plants

n, m = map(int, input().split())  # Read the input
print(min_replanted_plants(n, m))  # Print the result
