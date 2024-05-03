import sys

def solve():
    n, m = map(int, input().split())
    
    # Read the plants' information
    plants = []
    for _ in range(n):
        species, x = map(float, sys.stdin.readline().split())
        plants.append((species, x))

    # Sort the plants by their positions
    plants.sort(key=lambda x: x[1])

    # Initialize the borders and the current section's temperature
    borders = [0]
    temperatures = [0] * m

    # Iterate over the plants to place the borders
    for species, x in plants:
        if species != 0:
            while temperatures[species - 1] < temperatures[species]:
                borders.append(borders[-1])
                temperatures[species] += 1
        else:
            borders[-1] = x

    # Calculate the minimum number of replantings needed
    min_replantings = sum((b2 - b1) for (b1, t), (b2, _) in zip(borders[:-1], borders[1:]))

    return min_replantings


if __name__ == "__main__":
    print(solve())
