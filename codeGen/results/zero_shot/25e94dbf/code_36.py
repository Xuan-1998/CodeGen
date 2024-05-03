def max_distance(commands, n):
    distance = 0
    turn_count = 0
    
    for command in commands:
        if command == "F":
            distance += 1
        elif command == "T" and turn_count < n:
            distance -= turn_count * 2
            turn_count += 1
    
    return distance

# Example usage
commands = ["F"] * 10 + ["T", "F"] * 5
n = 3

print(max_distance(commands, n))
