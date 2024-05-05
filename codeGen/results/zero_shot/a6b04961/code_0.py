import sys

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

max_beauty = 0
tail_length = 0
spines = set()

# Iterate over all possible tails
for i in range(n):
    # Start a new tail at vertex i
    current_tail = [i]
    while True:
        # Find the next vertex in the tail
        for j in edges:
            if j[0] == current_tail[-1]:
                current_tail.append(j[1])
                break
        else:
            # No more edges to extend the tail
            break

        # Update the length of the tail
        tail_length = len(current_tail)

        # Find the maximum number of spines for this tail
        max_spines = 0
        for edge in edges:
            if edge[0] in current_tail and edge[1] not in current_tail:
                max_spines += 1

        # Update the maximum beauty
        beauty = tail_length * max_spines
        if beauty > max_beauty:
            max_beauty = beauty

print(max_beauty)
