# Step 1: Read input
n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Step 2: Initialize the maximum amount of gasoline that Nut can have at each city
max_gasoline = [0] * (n+1)

# Step 3: DFS from the first city to calculate the maximum amount of gasoline that Nut can have at each city
def dfs(city):
    if max_gasoline[city]:
        return max_gasoline[city]
    
    for road in roads:
        if road[0] == city:
            next_city = road[1]
            c = road[2]
            remaining_gasoline = w[city-1] - c
            if remaining_gasoline >= 0:
                max_gasoline[city] = max(dfs(next_city) + remaining_gasoline, w[city-1])
    return max_gasoline[city]

# Step 4: Print the maximum amount of gasoline that Nut can have at the end of the path
print(max(1 for _ in range(n)))
