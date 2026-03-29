===BEGIN CODE===
from collections import defaultdict

def simulate_sequence(sequence):
    n = len(sequence)
    memo = defaultdict(int)

    def recursive_simulation(x, y):
        if x > n or x <= 0:
            return -1
        state = (x, y)
        if state in memo:
            return memo[state]
        new_x = min(x + sequence[x], n) if x < n else -1
        new_y = y + sequence[x]
        value = recursive_simulation(new_x, new_y)
        if value == -1:
            return -1
        new_x -= sequence[new_x]
        new_y += sequence[new_x]
        memo[state] = recursive_simulation(new_x, new_y)
        return memo[state]

    for i in range(2, n + 1):
        print(recursive_simulation(i, 0))

===END CODE===
