import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def tarjan(n, graph):
    index = [0] * n
    lowlink = [0] * n
    on_stack = [False] * n
    stack = []
    scc_count = 0
    scc_indegree = defaultdict(int)
    scc_outdegree = defaultdict(int)
    
    def strongconnect(v, idx):
        nonlocal scc_count
        index[v] = idx
        lowlink[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True
        
        for w in graph[v]:
            if index[w] == 0:
                strongconnect(w, idx)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])
        
        if lowlink[v] == index[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break
            scc_count += 1
    
    idx = 1
    for v in range(n):
        if index[v] == 0:
            strongconnect(v, idx)
    
    for v in range(n):
        for w in graph[v]:
            if lowlink[v] != lowlink[w]:
                scc_indegree[lowlink[w]] += 1
                scc_outdegree[lowlink[v]] += 1
    
    return scc_count, scc_indegree

def main():
    input_lines = sys.stdin.readlines()
    current_line = 0
    
    while current_line < len(input_lines):
        n = int(input_lines[current_line].strip())
        current_line += 1
        
        graph = defaultdict(list)
        for i in range(n):
            line = list(map(int, input_lines[current_line].strip().split()))
            current_line += 1
            for j in line[1:]:
                graph[j-1].append(i)
        
        scc_count, scc_indegree = tarjan(n, graph)
        
        # Count the number of SCCs that have no incoming edges
        reads_required = sum(1 for i in range(scc_count) if scc_indegree[i] == 0)
        
        print(reads_required)

if __name__ == "__main__":
    main()
