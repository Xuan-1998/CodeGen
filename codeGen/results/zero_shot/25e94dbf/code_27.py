def max_distance(commands, n):
    pos = 0  # initial position (0)
    max_dist = 0  # maximum distance traveled

    for i in range(len(commands)):
        if commands[i] == "F":
            pos += 1  # move forward 1 unit
            max_dist = max(max_dist, pos)  # update maximum distance
        elif commands[i] == "T" and n > 0:
            # modify command to move forward instead of turning around
            commands[i] = "F"
            n -= 1

    return max_dist

# Example usage:
commands = ["FFFT", "FFFFT"]  # sample list of turtle commands
n = 2  # number of commands that can be modified

print(max_distance(commands, n))
