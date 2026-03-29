def program_sequence(n, sequence):
    memo = {}

    def transition(state):
        x, y = state
        if (x, y) in memo:
            return memo[(x, y)]
        
        next_x = x + sequence[x - 1]
        next_y = y + sequence[x - 1]
        
        memo[(x, y)] = ((next_x, next_y), (max(0, next_x - 1), next_y + sequence[next_x - 1]))
        
        return memo[(x, y)]

    for x in range(2, n + 1):
        state = (1, 0)
        while True:
            state = transition(state)
            if state[0] <= 0 or state[0] > n:
                break
        print(state[1])
