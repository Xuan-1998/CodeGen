tails = []
for start in range(n):
    current_vertex = start
    tail = [start]
    while True:
        for edge in edges:
            if edge[0] == current_vertex:
                next_vertex = edge[1]
                break
        else:
            # No more edges connect to the current vertex; this is a new spine.
            spines += 1
            break
        tail.append(next_vertex)
        current_vertex = next_vertex

        if len(tail) > max_tail_length:
            max_tail_length = len(tail)

    tails.append((tail, spines))

max_beauty = 0
for tail, spines in tails:
    beauty = len(tail) * spines
    if beauty > max_beauty:
        max_beauty = beauty

print(max_beauty)
