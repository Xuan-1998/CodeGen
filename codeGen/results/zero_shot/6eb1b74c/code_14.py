import sys

def solve():
    t = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    s = [sys.stdin.readline().strip() for _ in range(n)]
    
    indices = {}
    for i, si in enumerate(s):
        for j, c in enumerate(t):
            if c == si[0]:
                indices[(j, si)] = i
    
    s.sort(key=len)
    min_steps = 0
    for si in s:
        max_coverage = sum(1 for j, c in enumerate(t) if c == si[0])
        if not (max_coverage == 0 and si in indices):
            min_steps += max_coverage
    
    if min_steps == 0:
        print(-1)
    else:
        print(min_steps)
        for j in range(min_steps):
            w_j = -1
            p_j = -1
            for i, (p, si) in enumerate(sorted(indices.items(), key=lambda x: x[0])):
                if j < i:
                    continue
                if j == i or w_j == -1:
                    w_j = indices[(p, si)]
                    p_j = p
                    break
            print(f"{w_j} {p_j}")

if __name__ == "__main__":
    solve()
