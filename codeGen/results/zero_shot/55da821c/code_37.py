import sys

def solve():
    n, m = map(int, input().split())
    plants = [[i, x] for i, x in zip(map(int, input().split()), [float(x) for x in input().split()])]

    # Group plants by species and reorder within each section
    sorted_plants = [[] for _ in range(m)]
    for plant in plants:
        species, position = plant
        sorted_plants[species-1].append(position)

    # Calculate the minimum number of replantings
    min_replantings = 0
    prev_section_end = 0
    for section in range(1, m):
        min_replantings += len(sorted_plants[section-1]) - (len(sorted_plants[prev_section_end]) if prev_section_end > 0 else 0)
        prev_section_end = section

    print(min_replantings)

if __name__ == "__main__":
    solve()
