import re
from collections import deque

def solve():
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    # Initialize a dictionary to store the frequency of each string
    freq = {s: 0 for s in strings}

    # Count the frequency of each string
    for s in strings:
        freq[s] += t.count(s)

    # If it's impossible to color all letters, output -1
    if any(f > 0 for f in freq.values()):
        return -1

    m = 0
    used_strings = []
    for s in sorted(freq.keys(), key=lambda x: len(x), reverse=True):
        while re.search(s, t):
            pos = deque(re.finditer(s, t))
            last_pos = None
            while pos:
                last_pos = next(pos).start()
                if last_pos < m or not used_strings:
                    break
                pos.popleft()
            if last_pos is not None:
                used_strings.append(s)
                m += 1
                t = re.sub(s, '', t)

    return m

print(solve())
