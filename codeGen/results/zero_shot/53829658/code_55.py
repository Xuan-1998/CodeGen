# Step 1: Read the input
n = int(input())
roads = []
for _ in range(n-1):
    road = list(map(int, input().split()))
    roads.append(road)

# Step 2: Create a dictionary for each city and initialize the parent and rank of each city.
city_dict = {}
parent_dict = {}
rank_dict = {}
for i in range(1, n+1):
    city_dict[i] = i
    parent_dict[i] = i
    rank_dict[i] = 0

# Step 3: Use Union-Find to union the roads and find the root of each road.
def find(city):
    if city != parent_dict[city]:
        parent_dict[city] = find(parent_dict[city])
    return parent_dict[city]

def union(city1, city2):
    root1 = find(city1)
    root2 = find(city2)
    if rank_dict[root1] > rank_dict[root2]:
        parent_dict[root2] = root1
    else:
        parent_dict[root1] = root2
        if rank_dict[root1] == rank_dict[root2]:
            rank_dict[root2] += 1

for road in roads:
    union(road[0], road[1])

# Step 4: Calculate the minimum number of roads to be reversed.
min_inversed_roads = n-1
parent_root = find(1)

# Step 5: Find all possible ways to choose the capital and print them out.
possible_capitals = []
for i in range(1, n+1):
    if parent_dict[i] == parent_root:
        possible_capitals.append(i)
print(len(possible_capitals))
print(" ".join(map(str, possible_capitals)))
