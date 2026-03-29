import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        edges = []
        for _ in range(n-1):
            ui, vi = map(int, sys.stdin.readline().split())
            edges.append((ui, vi))

        # Sort edges by XOR of nodes at either end
        edges.sort(key=lambda x: a[x[0]] ^ a[x[1]])

        components = []
        component_xor = 0
        for edge in edges:
            if len(components) <= k-1:
                if not any(x[0] == edge[0] or x[1] == edge[1] for x in components):
                    components.append(edge)
                    component_xor ^= a[edge[0]] ^ a[edge[1]]
                else:
                    break
            else:
                break

        # Check if all components have consistent XOR
        xor_counts = {}
        for component in components:
            xor = a[component[0]] ^ a[component[1]]
            xor_counts[xor] = xor_counts.get(xor, 0) + 1
        if len(xor_counts) == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
