def max_distance(commands, n):
    directions = {'T': 1, 'F': -1}
    memo = {}

    def recursive_max_distance(i, j, direction):
        if (i, j, direction) in memo:
            return memo[(i, j, direction)]

        if i == len(commands):
            return 0

        max_dist = 0
        for k in range(n + 1):
            new_direction = direction * directions[commands[i]]
            dist = recursive_max_distance(i + 1, j - k, new_direction)
            max_dist = max(max_dist, dist + k)

        memo[(i, j, direction)] = max_dist
        return max_dist

    return recursive_max_distance(0, n, 1)
