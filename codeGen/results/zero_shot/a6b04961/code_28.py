# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Sort edges by endpoint
edges.sort(key=lambda x: x[0])

# Initialize variables
tail = []
spines = set()
max_beauty = 0

# Try to build the tail
for edge in edges:
    u, v = edge
    if not tail or u == tail[-1]:
        tail.append(u)
        if v not in tail:
            spines.add(edge)
    else:
        break

# Calculate the beauty of this hedgehog
beauty = len(tail) * (len(spines) + 1)

# Update max_beauty
max_beauty = max(max_beauty, beauty)

# Try to extend the tail and update max_beauty
while edges:
    edge = edges.pop(0)
    u, v = edge
    if not tail or u == tail[-1]:
        tail.append(u)
        if v not in tail:
            spines.add(edge)
        else:
            break
    else:
        break

# Calculate the beauty of this hedgehog
beauty = len(tail) * (len(spines) + 1)

# Update max_beauty
max_beauty = max(max_beauty, beauty)

print(max_beauty)
