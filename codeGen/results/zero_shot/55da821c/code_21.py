import sys

def min_replants(n, m):
    sections = []
    for i in range(n):
        s_i = int(sys.stdin.readline().split()[1])
        if len(sections) <= s_i - 1:
            sections.append([i + 1])  # 1-based indexing
        else:
            sections[s_i - 1].append(i + 1)
    return n - sum(len(s) for s in sections)

n, m = map(int, sys.stdin.readline().split())
print(min_replants(n, m))
