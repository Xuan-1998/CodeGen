import sys

def f(v, dp):
    if (v, 0) in dp:
        return dp[(v, 0)]
    
    min_recomps = max_recomps = 0
    
    for edge in edges:
        u, v_edge = edge
        if u != v and v_edge == v:
            recomps_needed = f(u, dp)
            if recomps_needed[1] > 0:  # If we didn't recalculate the previous time
                min_recomps += 1
            else:  # If we did recalculate the previous time
                max_recomps = max(max_recomps, recomps_needed[1])
    
    dp[(v, 0)] = (min_recomps, max_recomps)
    return dp[(v, 0)]

def main():
    n, m = map(int, input().split())
    edges = [(int(u), int(v)) for _ in range(m) for u, v in [input().split()]]
    
    s, t = map(int, input().split())
    path = list(map(int, input().split()))
    
    dp = {}
    
    min_recomps = max_recomps = 0
    for vertex in path:
        recomps_needed = f(vertex, dp)
        min_recomps = min(min_recomps, recomps_needed[0])
        max_recomps = max(max_recomps, recomps_needed[1])
    
    print(min_recomps, max_recomps)

if __name__ == "__main__":
    main()
