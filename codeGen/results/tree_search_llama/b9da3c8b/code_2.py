import sys

n = int(sys.stdin.readline())
officers = 0
untreated_crimes = 0

for event in map(int, sys.stdin.readline().split()):
    if event == -1:  # Crime occurred
        officers -= 1
        if officers < 0:
            untreated_crimes += 1
    else:  # New officers recruited
        officers += event

print(untreated_crimes)
