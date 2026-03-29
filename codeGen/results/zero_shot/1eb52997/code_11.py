import sys

T = int(sys.stdin.readline())
grid = {}

for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(N):
        row = sys.stdin.readline().strip()
        for j, char in enumerate(row):
            grid[(i, j)] = char

empty_cells = 0
for i in range(N):
    for j in range(N):
        if grid[(i, j)] == '.':
            east_count = 1
            while j + east_count < N and grid[(i, j + east_count)] == '.':
                east_count += 1
            empty_cells += east_count

print(empty_cells)
