import sys

def read_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    return n, m, edges

n, m, edges = read_input()

dp = {(0, set()): 1}

for u, v in edges:
    used_edges = dp.keys()[-1][1]
    path_length = len(dp.keys()[-1][0])
    
    new_path = dp[(dp.keys()[-1][0] + [v], used_edges | {(u, v)})].path
    new_used_edges = dp[(dp.keys()[-1][0] + [v], used_edges | {(u, v)})].used_edges
    
    if v in new_path:
        beauty = dp.get((new_path, new_used_edges), (0, set()))[1]
    else:
        beauty = 0
    
    dp[(new_path, new_used_edges)] = path_length * beauty

print(max(dp.values(), key=lambda x: x[1]))
