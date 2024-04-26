import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

def find_max_road_in_cycle(n, roads):
    uf = UnionFind(n)
    max_road = (0, 0, 0)  # (length, town1, town2)
    total_inconvenience = 0
    for u, v, l in roads:
        if not uf.union(u-1, v-1):
            if l > max_road[0]:
                max_road = (l, u, v)
        total_inconvenience += l
    return max_road, total_inconvenience

def main():
    n = int(input().strip())
    roads = [tuple(map(int, input().strip().split())) for _ in range(n)]
    max_road, total_inconvenience = find_max_road_in_cycle(n, roads)
    print(total_inconvenience - max_road[0])

if __name__ == "__main__":
    main()
