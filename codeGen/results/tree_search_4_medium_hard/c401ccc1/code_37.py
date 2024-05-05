import heapq

def infinite_zoo_queries(q):
    # Initialize a priority queue with all vertices at distance 0 from v
    pq = [(0, v) for _ in range(q)]
    heapq.heapify(pq)

    for u, v in [int(x) for x in input().split() for _ in range(q)]:
        # If u is equal to v, return "YES" because there's a path from u to itself
        if u == v:
            print("YES")
        else:
            while pq:
                d, w = heapq.heappop(pq)
                if w == v:
                    print("YES")
                    break
                for neighbor in range(w+1):
                    if (w & neighbor) == neighbor and not visited[neighbor]:
                        heapq.heappush(pq, (d+1, neighbor))
            else:
                print("NO")

if __name__ == "__main__":
    q = int(input())
    infinite_zoo_queries(q)
