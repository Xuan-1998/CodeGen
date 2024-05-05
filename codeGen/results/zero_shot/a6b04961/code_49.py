import sys

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))
adj_list = [[] for _ in range(n + 1)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

longest_path = []
def dfs(current, path):
    global longest_path
    if len(path) > len(longest_path):
        longest_path = list(path)
    for neighbor in adj_list[current]:
        if neighbor not in path:
            dfs(neighbor, path + [neighbor])

longest_path = []
for i in range(n + 1):
    dfs(i, [i])

max_beauty = 0
def max_spines(tail):
    global longest_path
    for i in range(len(longest_path) - 1):
        if longest_path[i] in tail:
            for j in range(i + 1, len(longest_path)):
                if longest_path[j] not in tail:
                    beauty = (len(tail)) * (j - i)
                    max_beauty = max(max_beauty, beauty)
    return max_beauty

max_beauty = 0
for path in [longest_path]:
    max_beauty = max(max_beauty, max_spines(path))
print(max_beauty)
