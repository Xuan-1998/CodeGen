from collections import defaultdict

def simulate_program(sequence):
    # Initialize the memoization dictionary
    memo = defaultdict(lambda: -1)

    def dfs(x, y):
        if (x, y) not in memo:
            if x <= 0 or x > len(sequence):
                return 0
            new_x = x + sequence[x]
            new_y = y + sequence[x]
            memo[(x, y)] = max(dfs(new_x - sequence[x], new_y), dfs(new_x, new_y))
        return memo[(x, y)]

    # Start with the initial state (n-1, 0)
    n = len(sequence) + 1
    return dfs(n-1, 0)

# Read input from standard input
n = int(input())
sequence = list(map(int, input().split()))

# Simulate the program for each sequence and print the results
for i in range(len(sequence)):
    print(simulate_program(sequence[:i+1]))
