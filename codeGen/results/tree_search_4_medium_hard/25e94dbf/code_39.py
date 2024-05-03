def max_distance(commands, n):
    dp = {(i, j): 0 for i in range(len(commands)) for j in range(n + 1)}

    for i in range(1, len(commands) + 1):
        if commands[i - 1] == 'F':
            dp[(i, n)] = dp.get((i - 1, n), 0) + 1
        elif i > 0 and j > 0:
            min_mods = min(j, i)
            for k in range(min_mods):
                dp[(i, j)] = max(dp.get((i - 1, j - 1), 0) - 1, dp.get((i - 1, j), 0))

    return dp.get((len(commands), n), 0)

commands = input().strip()
n = int(input())
print(max_distance(commands, n))
