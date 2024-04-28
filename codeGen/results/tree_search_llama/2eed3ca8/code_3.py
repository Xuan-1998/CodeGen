def is_circular(commands):
    x, y = 0, 0
    direction = 'North'
    
    for command in commands:
        if command == 'Forward':
            if direction == 'North': y += 1
            elif direction == 'South': y -= 1
            elif direction == 'East': x += 1
            elif direction == 'West': x -= 1
        elif command == 'Turn Left':
            if direction == 'North': direction = 'West'
            elif direction == 'South': direction = 'East'
            elif direction == 'East': direction = 'North'
            elif direction == 'West': direction = 'South'
        elif command == 'Turn Right':
            if direction == 'North': direction = 'East'
            elif direction == 'South': direction = 'West'
            elif direction == 'East': direction = 'South'
            elif direction == 'West': direction = 'North'
    
    return 'Circular' if (x, y) in [(0, 0)] else 'Not Circular'

commands = input().split()
print(is_circular(commands))
