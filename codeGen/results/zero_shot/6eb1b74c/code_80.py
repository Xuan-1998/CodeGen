import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

min_steps = 0
result = []

for s in strings:
    start_idx = 0
    while True:
        idx = text.find(s, start_idx)
        if idx == -1:
            break
        start_idx = idx + 1
        result.append((strings.index(s) + 1, idx))

min_steps = len(set([s for s in [result[i][0] for i in range(len(result))]]))

print(min_steps)
for pair in result:
    print(*pair)
