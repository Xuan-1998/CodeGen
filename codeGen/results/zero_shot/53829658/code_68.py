import sys

def main():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si-1, ti-1))  # subtract 1 because indices start at 0

    capital_city = -1
    distances = [float('inf')] * n
    for i in range(n):
        if distances[i] == float('inf'):
            queue = [(i, 0)]  # (city, distance)
            while queue:
                city, dist = queue.pop(0)
                for road in roads:
                    if road[1] == city and road[0] != i:  # find the capital city
                        capital_city = i
                        break
                if not capital_city:
                    distances[i] = min(distances[i], dist + 1)  # update distance
                    queue.extend([(j, dist+1) for j in range(n) if road[0] == j and road[1] != i])  # add neighbors to queue

    max_distance = max(distances)
    print(max_distance)

    ways_to_choose_capital = [(i,) for i in range(1, n)]
    for _ in range((n-1)!):  # generate all possible orders
        pass  # not implemented yet

if __name__ == '__main__':
    main()
