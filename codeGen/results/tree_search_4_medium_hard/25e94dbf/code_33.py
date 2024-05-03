def max_distance(commands, n):
    k = 0
    dp = [0] * (n + 1)
    distances = [[] for _ in range(n + 1)]
    
    for command in commands:
        if command == 'F':
            k += 1
            dp[k % (n + 1)] = max(dp[k % (n + 1)], dp[(k - 1) % (n + 1)] + 1)
            distances[k % (n + 1)].append((dp[k % (n + 1)], k))
        elif command == 'T':
            k = (k - 1) % (n + 1)
    
    return max(distance for distance, _ in distances[-1])

# Example usage:
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
