# Initialize a dictionary to store the in-degrees of all cities
in_degrees = {}
for _ in range(n-1):
    si, ti = map(int, input().split())
    if si not in in_degrees:
        in_degrees[si] = 0
    if ti not in in_degrees:
        in_degrees[ti] = 0
    in_degrees[si] += 1

# Find the city with maximum in-degree
capital = max(in_degrees, key=in_degrees.get)

# Print the minimum number of roads to be reversed
min_reversed_roads = n - len(in_degrees) - 1
print(min_reversed_roads)

# Initialize a list to store all possible ways to choose the capital
ways_to_chose_capital = []
def dfs(current_city, path, num_reversed_roads):
    if current_city == capital:
        ways_to_chose_capital.append(path)
    else:
        for predecessor in range(n+1):
            if predecessor != current_city and in_degrees[predecessor] > 0:
                in_degrees[predecessor] -= 1
                dfs(predecessor, path + [current_city], num_reversed_roads + 1)
                in_degrees[predecessor] += 1

dfs(1, [], 0)

# Print all possible ways to choose the capital
for way in ways_to_chose_capital:
    print(*way)
