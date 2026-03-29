===BEGIN CODE===
from collections import deque

def solve(t, s):
    n = len(s)
    m = [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]
    m[0] = [0] * (n + 1)

    pq = deque([(0, set())])

    while pq:
        pos, substrings = pq.popleft()
        if pos >= len(t):
            break

        for i, substring in enumerate(s):
            if substring in substrings and t[pos:].startswith(substring):
                new_substrings = substrings - {substring}
                m[pos + len(substring)][len(new_substrings)] = min(m[pos + len(substring)][len(new_substrings)], m[pos][len(substrings)] + 1)
                pq.append((pos + len(substring), new_substrings))

    if all(x != float('inf') for x in m[-1]):
        steps = m[-1].index(min(m[-1])) + 1
        used_substrings = [(j, i) for j, x in enumerate(m[-2]) for i, y in enumerate(x) if y == steps - 1]
        return steps, '\n'.join(f'{w} {p}' for w, p in used_substrings)
    else:
        return '-1'

# Test cases
t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]
print(solve(t, s))
