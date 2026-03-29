from sys import stdin

def has_consecutive_ones(n):
    # Your implementation here
    pass

def solve():
    n = int(stdin.readline())
    dp_state = [0] * (n + 1)

    for i in range(1, n + 1):
        if not has_consecutive_ones(i):
            dp_state[i] = dp_state[i - 1] + 1
        else:
            dp_state[i] = dp_state[i - 1]

    return dp_state[n]

print(solve())
