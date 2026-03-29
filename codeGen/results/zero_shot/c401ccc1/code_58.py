def infinite_zoo_queries():
    q = int(input())  # Read number of queries

    for _ in range(q):
        u, v = map(int, input().split())  # Read query (u, v)

        if u & v == v:  # Check condition $u\&v=v$
            print("YES")  # Path exists from u to v
        else:
            print("NO")  # No path from u to v

infinite_zoo_queries()
