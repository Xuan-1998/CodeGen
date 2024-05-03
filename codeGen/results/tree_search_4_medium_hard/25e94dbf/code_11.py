def max_distance(commands, n):
    memo = {}

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == 0:
            return 0

        prev_k = k - 1 if commands[i - 1] == 'F' else k
        dist = dp(i - 1, prev_k)

        if k > n:
            return dist

        # Modify the current command
        if commands[i - 1] == 'T':
            modified_dist = dp(i - 1, prev_k) + 1
        elif commands[i - 1] == 'F':
            modified_dist = dp(i - 1, k) + 1
        else:
            raise ValueError("Invalid command")

        # Store the result and return
        memo[(i, k)] = max(dist, modified_dist)
        return memo[(i, k)]

    return dp(len(commands), n)

# Example usage
commands = "TTFF"
n = 2
print(max_distance(commands, n))  # Output: 4
