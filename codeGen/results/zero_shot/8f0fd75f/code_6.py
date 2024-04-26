import sys

def read_input():
    n = int(input().strip())
    coordinates = list(map(int, input().strip().split()))
    durabilities = list(map(int, input().strip().split()))
    return n, coordinates, durabilities

def find_min_durability(n, coordinates, durabilities):
    # Check if the ordinary points can already support the ceiling
    for i in range(1, n + 1):
        if coordinates[i] - coordinates[i - 1] > durabilities[i - 1]:
            break
    else:
        # If all points can support the ceiling, no new point is needed
        return 0
    
    # Find the minimum durability needed for a new point
    min_durability = 0
    for i in range(1, n + 1):
        segment_length = coordinates[i] - coordinates[i - 1]
        if segment_length > durabilities[i - 1]:
            min_durability = max(min_durability, segment_length - durabilities[i - 1])
    
    return min_durability

def main():
    n, coordinates, durabilities = read_input()
    min_durability = find_min_durability(n, coordinates, durabilities)
    print(min_durability)

if __name__ == "__main__":
    main()
