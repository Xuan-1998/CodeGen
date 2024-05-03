def max_distance(commands, n):
    memo = {(0,): 0}

    for i in range(1, len(commands) + 1):
        for j in range(min(i, n) + 1):
            if (j,) not in memo:
                memo[(j,)] = 0
            if commands[i-1] == 'F':
                dp = memo.get((j-1,), 0)
                memo[(j,)] = max(memo[(j-1,)], dp + 1)
            else:
                for k in range(j+1):
                    memo[(k,)] = 0
                memo[(j,)] = max(memo[(i-1, j-k)].get(k, 0) + 1 for k in range(j))

    return memo.get((n,), 0)

# Example usage:
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
