# Step 1: Read the input
n = int(input())
roads = []
for i in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

# Step 2: Create a graph data structure
graph = {}
for road in roads:
    if road[0] not in graph:
        graph[road[0]] = []
    if road[1] not in graph:
        graph[road[1]] = []
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

# Step 3: Find the capital city
capital_city = None
for city, neighbors in graph.items():
    if len(neighbors) == 1:
        capital_city = city
        break

# Step 4: Count the minimum number of roads to be reversed
min_reversals = float('inf')
reversals = []
def count_reversals(city):
    global min_reversals, reversals
    if len(graph[city]) > 0:
        for neighbor in graph[city]:
            count_reversals(neighbor)
        if len(graph[city]) > 1 or (len(graph[city]) == 1 and city != capital_city):
            min_reversals = min(min_reversals, len(graph[city]))
            reversals.append(city)

count_reversals(capital_city)

# Step 5: Print the output
print(min_reversals)
print(' '.join(map(str, reversals)))
