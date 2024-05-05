import sys
import re

cases = []
while True:
    t = sys.stdin.readline().strip()
    if not t: break
    n = int(sys.stdin.readline())
    s = [sys.stdin.readline().strip() for _ in range(n)]
    cases.append((t, n, s))

for t, n, s in cases:
    data = create_data_structure(t, s)
    m = min_steps(data)
    if not t or m == -1:
        print(-1)
    else:
        for j in range(m):
            max_pos = 0
            max_str = None
            for i, pos_list in data.items():
                if pos_list and pos_list[0] > max_pos:
                    max_pos = pos_list[0]
                    max_str = i
            print(max_str, pos_list[0])
