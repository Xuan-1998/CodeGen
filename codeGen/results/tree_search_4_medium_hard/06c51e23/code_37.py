from math import ceil

n, t = map(int, input().split())
fraction = float(''.join(map(str, map(int, input().split(',')))))

state = [[0.0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    state[i][0] = fraction

for j in range(1, t + 1):
    state[0][j] = state[0][j - 1]

for i in range(1, n + 1):
    for j in range(min(i + 1, t + 1), 0, -1):
        if fraction < ceil(fraction):
            state[i][j] = max(state[i][j - 1], state[i - 1][j - 1] + (fraction % 1).quantize(0.01))
        else:
            state[i][j] = state[i][j - 1]

print('{:.5f}'.format(state[n][t]))
