n = int(input())  # read the number of cities
roads = []  # list of roads

# read the descriptions of the roads
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))  # add each road to the list

# calculate the minimum number of reversed roads for each possible capital
min_reversed = float('inf')  # initialize the minimum with infinity
capitals = []  # list of possible capitals

for city in range(1, n+1):
    reversed_roads = 0  # count the reversed roads for this capital
    parent = [city]  # keep track of the parent for each city

    for road in roads:
        si, ti = road
        if parent[si-1] == city:  # if this road is incoming to the current capital
            reversed_roads += 1  # increment the count
            parent[ti-1] = city  # update the parent of the other end city

    if reversed_roads < min_reversed:
        min_reversed = reversed_roads  # update the minimum
        capitals = [city]  # update the list of possible capitals
    elif reversed_roads == min_reversed:
        capitals.append(city)  # add this capital to the list if it's equal

print(min_reversed)  # print the minimum number of reversed roads
print(*capitals, sep=' ')  # print all possible ways to choose the capital
