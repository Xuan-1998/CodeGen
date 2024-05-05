import sys

n, m, c0, d0 = map(int, input().split())
stuffings = []

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

p = 0

# implement the optimization algorithm here (e.g., dynamic programming)

print(p)
