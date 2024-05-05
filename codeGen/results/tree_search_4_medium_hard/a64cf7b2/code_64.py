from collections import defaultdict

def max_vertices(T, n, edges):
    dp = {(0, 1): 1}
    
    for u, v, w in edges:
        for t in range(T, w - 1, -1):
            if (t, v) not in dp and (t - w, u) in dp:
                dp[(t, v)] = dp[(t - w, u)] + 1
    
    return dp.get((T, n), 0)

if __name__ == "__main__":
    n, m, T = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(max_vertices(T, n, edges))
