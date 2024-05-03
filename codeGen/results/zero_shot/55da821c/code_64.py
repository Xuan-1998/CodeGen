import sys

def min_replantings():
    n, m = map(int, input().split())
    plants = []
    for _ in range(n):
        s, x = map(float, input().split())
        plants.append((int(s), int(x)))

    # Sort plants by position (x)
    plants.sort(key=lambda x: x[1])

    # Initialize the replanting count
    replantings = 0

    # Iterate through the sorted plants and group them into sections
    for i in range(m):
        section_start = None
        for j, plant in enumerate(plants):
            if plant[0] == i + 1:
                if section_start is None:
                    section_start = j
                elif j > section_start:
                    replantings += j - section_start
                    break

    return replantings

print(min_replantings())
