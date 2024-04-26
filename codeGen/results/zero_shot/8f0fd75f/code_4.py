import sys

def read_input():
    n = int(input().strip())
    coordinates = list(map(int, input().strip().split()))
    durabilities = list(map(int, input().strip().split()))
    return n, coordinates, durabilities

def simulate_load_distribution(n, coordinates, durabilities):
    loads = [0] * (n + 2)
    for i in range(1, n + 1):
        loads[i] = coordinates[i + 1] - coordinates[i - 1]
    return loads

def find_min_durability(n, coordinates, durabilities, loads):
    min_durability_required = 0
    for i in range(1, n + 1):
        if loads[i] > durabilities[i - 1]:
            # Point i collapses, redistribute load to neighbors
            excess_load = loads[i] - durabilities[i - 1]
            if i - 1 > 0:
                loads[i - 1] += excess_load / 2
            if i + 1 <= n:
                loads[i + 1] += excess_load / 2
            loads[i] = durabilities[i - 1]
            min_durability_required = max(min_durability_required, excess_load)
    return min_durability_required

def main():
    n, coordinates, durabilities = read_input()
    loads = simulate_load_distribution(n, coordinates, durabilities)
    min_durability_required = find_min_durability(n, coordinates, durabilities, loads)
    print(min_durability_required)

if __name__ == "__main__":
    main()
