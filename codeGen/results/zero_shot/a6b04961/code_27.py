# Step 1: Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Step 2: Build an adjacency list representation of the graph
adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Step 3: Find all strongly connected components (SCCs) using Tarjan's algorithm
sccs = []
low = [n] * n
disc = [n] * n
on_stack = [False] * n
stack = []
time = 0

def strong_connect(v):
    low[v] = disc[v] = time
    stack.append(v)
    on_stack[v] = True
    time += 1
    for w in adj_list[v]:
        if disc[w] == n:
            strong_connect(w)
            low[v] = min(low[v], low[w])
        elif on_stack[w]:
            low[v] = min(low[v], disc[w])

def scc():
    global time
    for v in range(n):
        if disc[v] == n:
            strong_connect(v)

scc()
for i, c in enumerate(on_stack):
    if c:
        sccs.append(list(range(i+1, c+1)))

# Step 4: Find the maximum beauty by iterating over all SCCs and counting the number of spines
max_beauty = 0

def count_spines(scc):
    non_tail_edges = set()
    for u in scc:
        for v in adj_list[u]:
            if v not in scc:
                non_tail_edges.add((u, v))

    beauty = len(scc) * (len(sccs) - 1)
    for u, v in non_tail_edges:
        beauty += 1
    return beauty

max_beauty = max(count_spines(scc) for scc in sccs)

# Step 5: Print the maximum beauty
print(max_beauty)
