import sys

def main():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((s, x))

    plants.sort(key=lambda x: x[1])

    # Create a dictionary to store the count of each species
    species_count = {}
    for plant in plants:
        if plant[0] not in species_count:
            species_count[plant[0]] = 1
        else:
            species_count[plant[0]] += 1

    min_replants = 0
    prev_species = None
    for i, plant in enumerate(plants):
        if plant[0] != prev_species:
            min_replants += species_count[plant[0]]
        prev_species = plant[0]

    print(min_replants)

if __name__ == "__main__":
    main()
