import sys
from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def findMST(self):
        visited = [False] * self.V
        minHeap = [(0, 0)]  # (weight, vertex)
        mst_edges = []
        total_weight = 0
        
        while minHeap:
            weight, u = heapq.heappop(minHeap)
            if not visited[u]:
                visited[u] = True
                total_weight += weight
                for v, w in self.graph[u]:
                    if not visited[v]:
                        heapq.heappush(minHeap, (w, v))
                        mst_edges.append((u, v, w))
        return mst_edges, total_weight
    
    def maxEdgeInMST(self, mst_edges):
        return max(mst_edges, key=lambda x: x[2])

def main():
    n = int(sys.stdin.readline().strip())
    graph = Graph(n)
    
    for _ in range(n):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        graph.addEdge(u-1, v-1, w)
    
    mst_edges, total_weight = graph.findMST()
    u, v, max_weight = graph.maxEdgeInMST(mst_edges)
    
    # Remove the maximum weighted edge from the total weight of MST
    min_inconvenience = total_weight - max_weight
    print(min_inconvenience)

if __name__ == "__main__":
    main()
