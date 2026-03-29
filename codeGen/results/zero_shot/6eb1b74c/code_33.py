import sys

def solve():
    n = int(sys.stdin.readline())
    text = sys.stdin.readline().strip()
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    occurrences = {}
    for s in strings:
        start_idx = 0
        while True:
            idx = text.find(s, start_idx)
            if idx == -1:
                break
            occurrences[s] = occurrences.get(s, []) + [(idx, idx + len(s))]
            start_idx = idx + 1

    strings.sort(key=lambda s: len(occurrences.get(s, [])))

    m = 0
    result = []

    for s in strings:
        while occurrences.get(s, []):
            idx, _ = occurrences[s].pop(0)
            m += 1
            result.append((n - len(result), idx))

    print(m)
    for r in result:
        print(*r)

solve()
