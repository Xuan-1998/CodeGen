import sys

def main():
    n = int(sys.stdin.readline())
    roads = [[] for _ in range(n+1)]

    # Read road information and construct graph
    for i in range(1, n):
        si, ti = map(int, sys.stdin.readline().split())
        roads[si].append(ti)
        roads[ti].extend([si])

    # Find capital city with maximum in-degree
    capital = max(range(1, n+1), key=lambda x: len(roads[x]))

    # Calculate minimum number of roads to be reversed
    min_edges_to_reverse = max(len(road) for road in roads) - 1

    # Print results
    print(min_edges_to_reverse)
    print(capsule)

if __name__ == "__main__":
    main()
